import pytest


pytest.main([

    "step_definitions/test_signup_steps.py",

    "step_definitions/test_login_steps.py",

    "step_definitions/test_cart_steps.py",

    "step_definitions/test_checkout_steps.py",

    "-v"
])