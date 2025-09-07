# Setup Instructions for EC2 Deployment

1. SSH into your EC2 instance.
2. Install Python 3 and pip if not already installed:
   sudo yum update -y
   sudo yum install python3 -y

3. Upload your project files to the EC2 instance (use scp or git clone).

4. Navigate to your project directory:
   cd Gemimi_code_explainer

5. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

6. Install dependencies:
   pip install -r requirements.txt

7. Run the Flask app:
   python app.py

8. (Optional) To keep the app running, use tmux/screen or a process manager like gunicorn or supervisor.

9. Open port 5000 in your EC2 security group to allow external access.

10. Access the app at http://<your-ec2-public-ip>:5000/
