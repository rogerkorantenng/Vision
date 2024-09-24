# Table of Contents
- [Introduction](#nvidia-ai-workbench-introduction)
   - [Project Description](#project-description)
   - [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
   - [Using Local Development Environment](#using-local-development-environment)
   - [Using a Cloud Development Environment](#using-a-cloud-development-environment)

# NVIDIA AI Workbench: Introduction [![Open In AI Workbench](https://img.shields.io/badge/Open_In-AI_Workbench-76B900)](https://nvidia.github.io/workbench-example-hybrid-rag/clone_me.html)

## Project Description

This project aims to develop an application with the **google/vit-base-patch16-224** model, featuring a fully customizable **Gradio Image Recognition** interface. Key functionalities include:

- The ability to upload images or capture live photos for identification.
- Performing image recognition **locally** or **remote** by running inference directly on the model.


### Table 1: Default Supported Models by Inference Mode


## Prerequisites

- Familiarity with **Hugging Face** and its ecosystem.

---

## System Requirements
Below are the minimum and recommended system requirements for the project:

| vRAM  | System RAM | Disk Storage | vCPU         | GPU                   |
|-------|------------|--------------|--------------|-----------------------|
| 8 GB | 16 GB      | 70 GB        | Intel Core i7| At least 1 (optional) |



## Quickstart

### Using Local Development Environment

1. **Install and Set Up AI Workbench**: Begin by [installing and configuring](https://docs.nvidia.com/ai-workbench/user-guide/latest/installation/overview.html) AI Workbench on your local machine. Open the application and select a preferred location.

2. **Fork the Repository**: Fork this repository into your own GitHub account.

3. **Clone the Project in AI Workbench**:
   - Inside AI Workbench, click on **Clone Project**.
   - Enter the URL of your forked repository.
   - AI Workbench will clone the repository and build the project environment. This process may take several minutes.


4. **Start the Project**:
   - Click on **Start Environment** to launch the project container.
   - To open the Gradio app, select **Open VisionTrack** from the top right corner of the AI Workbench window. The app will open in your browser.

### Using a Cloud Development Environment

1. **Set Up an AWS EC2 Instance**:
   - Log in to your AWS Management Console.
   - Navigate to **EC2 Dashboard** > **Launch Instance**.
   - Choose an appropriate Amazon Machine Image (AMI), preferably one with an NVIDIA GPU, such as an NVIDIA Deep Learning AMI.
   - Select an instance type with sufficient GPU resources (e.g., `g4dn.xlarge`).
   - Configure your instance, including network settings and storage, according to your project requirements.
   - Review and launch the instance. Ensure you have a key pair for SSH access.

2. **Connect to Your EC2 Instance**:
   - Open a terminal on your local machine.
   - Connect to your EC2 instance using SSH:
     ```bash
     ssh -i /path/to/your-key.pem ec2-user@your-ec2-public-ip
     ```
   - Replace `/path/to/your-key.pem` with the path to your private key and `your-ec2-public-ip` with your instance's public IP address.

3. **Install and Set Up AI Workbench on the EC2 Instance**:
   - Once connected to your EC2 instance, update your system:
     ```bash
     sudo apt-get update
     sudo apt-get upgrade
     ```
   - Follow the [official NVIDIA guide](https://docs.nvidia.com/ai-workbench/user-guide/latest/installation/ubuntu-remote.html) to install and set up AI Workbench on your EC2 instance. This guide provides detailed instructions for remote installation on Ubuntu systems.

4. **Clone the Project in AI Workbench**:
   - Inside AI Workbench on the EC2 instance, click on **Clone Project**.
   - Enter the URL of your forked repository.
   - AI Workbench will clone the repository and build the project environment. This process may take several minutes.

5. **Start the Project**:
   - Click on **Start Environment** to launch the project container.
   - To open the Gradio app, select **Open VisionTrack** from the top right corner of the AI Workbench window. The app will open in your browser.
