from agents.requirements_agent import gather_requirements

request = "Build an online banking system for customers to transfer money and view transactions."

result = gather_requirements(request)

print(result)