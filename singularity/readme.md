## Download singularity image
singularity pull docker://masidocker/spiders:wholebody_v1_0_0

## Run singularity image
singularity exec -B {Your Input Folder}:/INPUTS -B {Your Ouput Folder}:/OUTPUTS deeplearning-DeepWholeBodySpider.simg /extra/run_deep_wholebody.sh

Your Input Folder: path to a folder which contains a single whole abdomen .nii.gz image

Your Ouput Folder: path to a folder which saves all output results
