#!/usr/bin/env python3
"""
Setup script for Netfix project
Run this after cloning to set up the project with sample data
"""

import os
import sys
import subprocess


def run_command(command, description):
    """Run a command and print status"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False


def main():
    print("🚀 Setting up Netfix project...")
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Run migrations
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        sys.exit(1)
    
    if not run_command("python manage.py migrate", "Applying migrations"):
        sys.exit(1)
    
    # Create sample services
    if not run_command("python manage.py create_sample_services", "Creating sample services"):
        print("⚠️  Warning: Failed to create sample services, but continuing...")
    
    print("\n🎉 Project setup completed!")
    print("\n📋 What was created:")
    print("   • Database tables")
    print("   • 3 sample company users")
    print("   • 3 sample services (Plumbing, Electrical, Gardening)")
    print("\n🔧 Next steps:")
    print("   1. Create a superuser: python manage.py createsuperuser")
    print("   2. Start the server: python manage.py runserver")
    print("   3. Visit http://127.0.0.1:8000/")
    print("\n💡 Sample company credentials (password: defaultpass123):")
    print("   • quickfix_plumbing@quickfixplumbing.com")
    print("   • info@sparkleelectric.com")
    print("   • hello@greengardens.com")


if __name__ == "__main__":
    main()
