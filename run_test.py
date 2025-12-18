#!/usr/bin/env python3
"""
Simple test runner for Automation Exercise Test Cases
"""

import sys
import os
from test_case_1_register_user import TestCase1RegisterUser


def main():
    """Main function to run the test"""
    print("🎯 Automation Exercise Test Runner")
    print("=" * 40)
    
    # Check if Chrome is available
    try:
        import subprocess
        result = subprocess.run(['google-chrome', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"✅ Chrome detected: {result.stdout.strip()}")
        else:
            print("⚠️ Chrome not found, trying chromium...")
            result = subprocess.run(['chromium-browser', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print(f"✅ Chromium detected: {result.stdout.strip()}")
            else:
                print("❌ Neither Chrome nor Chromium found!")
                print("Please install Google Chrome or Chromium browser.")
                return False
    except Exception as e:
        print(f"⚠️ Could not check browser version: {e}")
    
    print("=" * 40)
    
    # Run Test Case 1
    print("🚀 Executing Test Case 1: Register User")
    test = TestCase1RegisterUser()
    success = test.run_test()
    
    print("=" * 40)
    if success:
        print("🎉 TEST EXECUTION COMPLETED SUCCESSFULLY!")
        print("✅ All test steps passed")
        return True
    else:
        print("❌ TEST EXECUTION FAILED!")
        print("Please check the error messages above for details")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
