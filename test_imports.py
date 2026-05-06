#!/usr/bin/env python3

try:
    import gradio as gr
    print("✓ Gradio imported successfully")
except ImportError as e:
    print(f"✗ Gradio import failed: {e}")

try:
    import helper_functions as api
    print("✓ helper_functions imported successfully")
except ImportError as e:
    print(f"✗ helper_functions import failed: {e}")

try:
    import practo_integration
    print("✓ practo_integration imported successfully")
except ImportError as e:
    print(f"✗ practo_integration import failed: {e}")

try:
    import doctor_filter_by_degree as degree
    print("✓ doctor_filter_by_degree imported successfully")
except ImportError as e:
    print(f"✗ doctor_filter_by_degree import failed: {e}")

try:
    import agentops
    agentops.init()
    print("✓ agentops imported and initialized successfully")
except ImportError as e:
    print(f"✗ agentops import failed: {e}")
except Exception as e:
    print(f"✗ agentops init failed: {e}")

try:
    import initialize_crew as helper
    print("✓ initialize_crew imported successfully")
except ImportError as e:
    print(f"✗ initialize_crew import failed: {e}")

print("All basic imports completed.")