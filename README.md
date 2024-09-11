# Python OOP Programs

## Introduction

Hiya guys! Welcome to the **Python OOP Programs** repository, where you can create your own service using Python Object-Oriented Programming (OOP). 

Inside this repository, you'll find a collection of folders and a `main.py` file. Each folder contains a Python program, ranging from simple to complex, all of which are connected to the `main.py`. The `main.py` program is currently set up to run locally in the terminal. Once executed, you will be welcomed and introduced to a list of programs contributed by various developers from around the world.

As a contributor, your goal is to create a program in your specific folder and connect it to the `main.py`. If your contribution meets the criteria, I will add it to the main repository for others to see and use.

Though it might seem small, this repository is important. It's a platform where developers from anywhere can showcase their talents in OOP Python programming, expressing their creativity and skills. So, feel free to build, have fun, and make your mark!

Looking forward to seeing what you can do! 😊

---

# Contributing to the Project

If you'd like to contribute to the project, please follow these steps:

## Step-by-Step Instructions

1. **Fork the Repository**
   - Go to the [repository URL](YOUR_REPOSITORY_URL_HERE) on GitHub.
   - Click the `Fork` button in the top-right corner to create a copy under your GitHub account.

2. **Clone Your Forked Repository**
   - Open your terminal or command prompt.
   - Clone your forked repository:
     ```bash
     git clone https://github.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME.git
     ```
   - Navigate to the repository directory:
     ```bash
     cd REPOSITORY_NAME
     ```

3. **Create a New Folder for Your Service**
   - Inside the repository, create a new folder for your service:
     ```bash
     mkdir your_service
     ```
   - Inside this folder, create a file named `your_service.py`.

4. **Implement Your Service**
   - In `your_service.py`, implement your service as a class:
     ```python
     class YourService:
         def __init__(self):
             # Initialization code here

         def run(self):
             # Code to run the service here
     ```
   - Ensure that your class has a `run` method to simulate the service functionality.

5. **Add Your Service to `ServiceManager`**
   - Open `main.py` in the repository.
   - Import your new service at the top:
     ```python
     from your_service.your_service import YourService
     ```
   - Add your service to the `ServiceManager` class:
     ```python
     class ServiceManager:
         def __init__(self):
             self.your_service = YourService()
             self.mira_bank = MiraBank()  # Existing service

         def run(self):
             while True:
                 print('Hello, welcome to Mi-Global Network. What service would you like to use?')
                 print('1. MiraBank\n2. Your Service\n3. Exit')
                 choice = input("Choose 1/2/3: ")

                 if choice == "1":
                     self.mira_bank.run()
                 elif choice == "2":
                     self.your_service.run()
                 elif choice == "3":
                     print("Thank you for choosing our services!")
                     break
                 else:
                     continue
     ```
   - Update the options in the `run` method to include your service.

6. **Commit Your Changes**
   - Stage your changes:
     ```bash
     git add .
     ```
   - Commit with a meaningful message:
     ```bash
     git commit -m "Added YourService to ServiceManager"
     ```

7. **Push Your Changes**
   - Push your changes to your forked repository:
     ```bash
     git push origin main
     ```

8. **Create a Pull Request**
   - Go to your forked repository on GitHub.
   - Navigate to the `Pull Requests` tab and click `New Pull Request`.
   - Ensure the base repository is the original repository, with the base branch as `main`.
   - Compare it with your fork's `main` branch.
   - Click `Create Pull Request` and provide a description of your changes.

## Notes
- Follow the project’s coding standards and conventions.
- Test your service thoroughly before submitting a pull request.
- Submit a pull request only if your service is fully functional and integrates well with the existing services.

Thank you for contributing to the project!
