# Notion-Automated-Recon
Recon and writeup script synced to Notion's API to automate the writup process of reconaissence 

1. Go to https://www.notion.so/my-integrations and create a new integration.![image](https://user-images.githubusercontent.com/122157280/211153215-5e69b536-4483-46cf-8e52-7d283f3fd312.png)

2. Create the following!!

![image](https://user-images.githubusercontent.com/122157280/211155437-e4b5e4dc-e524-49da-9a03-feac0ee8303d.png)

Edit the notion.py script and add your Notion API key under the "Token" variable 
![image](https://user-images.githubusercontent.com/122157280/211155458-fe4f03a8-3f2d-46d0-8dcc-8c000735dcc0.png)
![image](https://user-images.githubusercontent.com/122157280/211155476-ea071657-cc68-4f2f-92b8-6225d693a555.png)

Next we need to add the parent page token of where the writups will be created. This can be found in the URL of the Notion Page and will be specific to your notion account:

![image](https://user-images.githubusercontent.com/122157280/211157411-9e969f7f-c025-458e-9ba2-adfbac83cc13.png)

![image](https://user-images.githubusercontent.com/122157280/211157504-10096467-1b17-4893-bd8a-dbedf8756f39.png)

This will go in the notion.py PARENT variable here:

![image](https://user-images.githubusercontent.com/122157280/211157605-af515291-f7d6-4e41-9977-1ee200b9c29b.png)

Lastly, under the parent page, click on the 3 dots and at the bottom we should see the custom integration we linked with the recon script and our API key:

![image](https://user-images.githubusercontent.com/122157280/211157795-6655bab8-89f4-4555-818b-99af4caf9776.png)

![image](https://user-images.githubusercontent.com/122157280/211157864-254ac198-27c1-44bd-8072-2547fe1ab083.png)

After enabling this connection the script should be set up for your own notion notes!
