# 🚀 Deployment Guide — Host Your Static Website on Amazon S3

This guide walks you through the exact steps to deploy your static website using the AWS Management Console.  
It is written for beginners and focuses on clarity, safety, and real-world AWS practices.

---

## ✅ Step 1: Create Your S3 Bucket

1. Log in to the AWS Management Console.
2. Search for **S3** in the top search bar.
3. Click **Create bucket**.
4. Choose:
   - **Bucket type:** General Purpose (default)
   - **Bucket name:** A globally unique, lowercase name  
     Example: `my-unique-cloud-match-game`
5. Leave all other settings as default.
6. Scroll down and click **Create bucket**.

---

## ✅ Step 2: Enable Static Website Hosting

1. Open your newly created bucket.
2. Go to the **Properties** tab.
3. Scroll to **Static website hosting** → click **Edit**.
4. Set:
   - **Static website hosting:** Enable  
   - **Hosting type:** Host a static website  
   - **Index document:** `index.html`
5. Click **Save changes**.

📌 **Important:**  
At the bottom of the Properties page, AWS will show a **Bucket website endpoint**.  
This is your public website URL — save it for later.

---

## ✅ Step 3: Allow Public Read Access (For Learning Only)

By default, S3 buckets block all public access.  
To allow visitors to view your website, you must temporarily open the bucket.

1. Go to the **Permissions** tab.
2. Under **Block public access**, click **Edit**.
3. Uncheck **Block all public access**.
4. Click **Save changes**.
5. Type `confirm` when prompted.

⚠️ **Security Warning (Beginner-Friendly Explanation)**  
This step makes your bucket public.  
This is okay for learning, but **never** do this in production.

Real-world deployments use:
- CloudFront  
- Origin Access Control (OAC)  
- Least privilege IAM policies  
- No `"Principal": "*"`  
- No `"Action": "s3:*"`  

---

## ✅ Step 4: Add a Public Read Bucket Policy

Now that public access is allowed, you must explicitly tell S3 to allow users to read your files.

1. Stay in the **Permissions** tab.
2. Scroll to **Bucket policy** → click **Edit**.
3. Paste this JSON policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"
        }
    ]
}
```
4. Replace YOUR-BUCKET-NAME-HERE with your actual bucket name.
5. Click Save changes.

#### 📌 Important:  
Keep the /* at the end — it allows access to all objects inside the bucket.

---
## ✅ Step 5: Upload Your Website Files

1. Go to the Objects tab.
2. Click Upload.
3. Click Add files and select:
    - index.html
    - style.css
    - script.js
    - Any images or assets
4. Do not upload the parent folder — upload the files directly.
5. Click Upload.

Once the upload succeeds:
- Open a new browser tab
- Paste your Bucket website endpoint from Step 2

Your website is now live globally 🎉

---

## 🎉 Deployment Complete!
You have successfully deployed a static website using Amazon S3.
This is a foundational cloud skill and a great milestone in your AWS learning journey.