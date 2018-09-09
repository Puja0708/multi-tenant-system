# multi-tenant-system

## setup

1. clone the repository :
    ```
        git clone https://github.com/Puja0708/multi-tenant-system.git
    ```

2.  make virtual environment (optional):
    ```
        virtualenv -p python3 venv

    ```

3. activate virtual environment and install dependencies
   ```
        source venv/bin/activate

        pip install -p requirements/<dev/staging/prod>.pip
   ```

4. Run Migrations
     ```
        ./manage.py migrate_schemas --shared  --settings=multi_tenant_system.settings.<dev/staging/prod>
     ```

5. Create superuser
     ```
        ./manage.py createsuperuser  --settings=multi_tenant_system.settings.<dev/staging/prod>
     ```


Now you can play around with this. In this project, `companies.models.Company` is the main tenant model.
You can create tenants from the django admin console.

6. Running test cases :
    ```
         ./manage.py test employees.tests --settings=multi_tenant_system.settings.dev
    ```


TODO :
    - auth for companies, employees etc (use DRF authentication_classes and permission_classes.
    - api tests