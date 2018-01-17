from dax import AutoSpider

name = 'wholebody_singularity'

version = '1.0.0'

exe_lang = 'bash'

inputs = [
    ("ct_file", "FILE", "Path to CT file")
]

outputs = [
    ("OUTPUTS/FinalResult/SpleenVol.txt","FILE","SPLEEN_VOL"),
    ("OUTPUTS/FinalSeg/keeplarge1_morpho1/GCN/Dice_norm/target_img/seg_view3.nii.gz","FILE","FINAL_SEG"),
    ("OUTPUTS/FinalSeg/keeplarge1_morpho1/GCN/Dice_norm/target_img/seg_view3_orig_seg.nii.gz","FILE","FINAL_SEG"),
    ("OUTPUTS/FinalResult/result.pdf","FILE","PDF")
]

code = r"""# Set environment
module load GCC Singularity

# Create INPUTS and OUTPUTS directories
mkdir ${temp_dir}/INPUTS
mkdir ${temp_dir}/OUTPUTS

mv ${ct_file} ${temp_dir}/INPUTS/CT.nii.gz

# Run singularity image
singularity exec -B ${temp_dir}/INPUTS:/INPUTS/ -B ${temp_dir}/OUTPUTS:/OUTPUTS/ /data/mcr/singularity/wholebody_v1_0_0/wholebody_v1_0_0.img /extra/run_deep_wholebody.sh"""

if __name__ == '__main__':
    spider = AutoSpider(
        name,
        inputs,
        outputs,
        code,
        version=version,
        exe_lang=exe_lang,
    )

    spider.go()
