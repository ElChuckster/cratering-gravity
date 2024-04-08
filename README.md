# cratering-gravity
EOSC 454 Final Project investigating how to model density profiles from gravity anomalies caused by Lunar cratering events.

To begin with, please install the environment file found within the repository (cratering-gravity.yml)

## Installation Instructions

To install the required dependencies for this project, you can create a Conda environment using the provided cratering-gravity.yml environment file.

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

```bash
git clone https://github.com/ElChuckster/cratering-gravity.git
```

2.1.***Navigate to the Repository***: Change the directory you're currently working in to the directory of the cloned repository on your device.

```bash
cd your-directory
```

2.2. ***Create the Conda Environment: Use Conda to create the new environment based on the .yml file

```bash
conda env create -f cratering-gravity.yml
```

2.3. ***Activate the Environment***: Once the installation has run, perform the following:

```bash
conda activate cratering-gravity
```

2.4. ***Verify the Installation***: To show that the environment has been successfully installed and has all the needed dependencies:

```bash
conda list
```

This project uses SimPEG gravity modules and possibly Fatiando a Terra. To familiarise yourself with these modules, tutorials/documentation have been provided below:

***SimPEG***: https://simpeg.xyz/user-tutorials/gravity-index

***Fatiando a Terra***: https://www.fatiando.org/

