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

6. Login to *django admin console* to create tenants (You can also do it using django shell. It is exactly like creating any django model object and saving it).

7. Create Employee Roles and Teams (using shell or their corresponding APIs/ Forms.

8. Create Employee.  


Now you can play around with this. In this project, `companies.models.Company` is the main tenant model.
You can create tenants from the django admin console.

6. Running test cases :
    ```
         ./manage.py test employees.tests --settings=multi_tenant_system.settings.dev
    ```


7. ## TESTING TENANCT ON LOCAL W/O A DOMAIN :
    - make an entry in the `/etc/hosts/` file mapping your localhost to a fake domain.
        eg : `127.0.0.1 example.com tenant1.example.com tenant2.example.com`.


TODO :
    - auth for companies, employees etc (use DRF authentication_classes and permission_classes.
    - api tests