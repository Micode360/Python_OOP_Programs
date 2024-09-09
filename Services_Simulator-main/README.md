# Contributing to the Project

If you would like to contribute to the project, please follow these steps:

## Step-by-Step Instructions

1. **Fork the Repository**
   - Go to the [repository URL](YOUR_REPOSITORY_URL_HERE) on GitHub.
   - Click on the `Fork` button in the top right corner of the page to create a copy of the repository under your GitHub account.

2. **Clone Your Forked Repository**
   - Open your terminal or command prompt.
   - Clone your forked repository using:
     ```bash
     git clone https://github.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME.git
     ```
   - Navigate to the repository directory:
     ```bash
     cd REPOSITORY_NAME
     ```

3. **Create a New Folder for Your Service**
   - Inside the repository, create a new folder for your service. For example:
     ```bash
     mkdir your_service
     ```
   - Inside this folder, create a file named `your_service.py`.

4. **Implement Your Service**
   - In the `your_service.py` file, implement your service as a class. For example:
     ```python
     class YourService:
         def __init__(self):
             # Initialization code here

         def run(self):
             # Code to run the service here
     ```
   - Make sure your service class has a `run` method that simulates the service's functionality.

5. **Add Your Service to `ServiceManager`**
   - Open the `main.py` file in the repository.
   - Import your new service at the top of the file:
     ```python
     from your_service.your_service import YourService
     ```
   - Add your service as an attribute in the `ServiceManager` class:
     ```python
     class ServiceManager:
         def __init__(self):
             self.your_service = YourService()
             self.mira_bank = MiraBank()  # Existing service

         def run(self):
             while True:
                 print('Hello welcome to mi-global network. What service do you like to use?')
                 print('1. Mirabank\n2. Your Service\n3. Exit')
                 choice = input("Choose 1/2/3: ")

                 if choice == "1":
                     self.mira_bank.run()
                 elif choice == "2":
                     self.your_service.run()
                 elif choice == "3":
                     print("Thank you for choosing our services")
                     break
                 else:
                     continue
     ```
   - Update the options in the `run` method to include your new service.

6. **Commit Your Changes**
   - Add your changes to the staging area:
     ```bash
     git add .
     ```
   - Commit your changes with a descriptive message:
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
   - Click on the `Pull Requests` tab.
   - Click on `New Pull Request`.
   - Ensure the base repository is set to the original repository and the base branch is `main`.
   - Compare it with your fork's `main` branch.
   - Click on `Create Pull Request` and provide a description of your changes.

## Notes
- Ensure your code follows the project's coding standards and conventions.
- Make sure to test your service thoroughly before submitting a pull request.
- Only submit a pull request if your service is fully functional and integrates properly with the existing services.

Thank you for contributing to the project!
