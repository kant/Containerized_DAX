## Download the docker image
You could use docker pull to download the docker image, which is publiclly released from docker hub
sudo docker pull masidocker/spiders:wholebody_v1_0_0

## Run the docker image
sudo nvidia-docker run -it --rm -v {Your Input Folder}:/INPUTS/ -v {Your Output Folder}:/OUTPUTS masidocker/spiders:wholebody_v1_0_0 /extra/run_deep_wholebody.sh

Your Input Folder: path to a folder which contains a single whole abdomen .nii.gz image

Your Ouput Folder: path to a folder which saves all output results
