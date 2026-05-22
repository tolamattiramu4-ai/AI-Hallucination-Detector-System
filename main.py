from verifier import verify_response

print("=== AI Hallucination Detector ===\n")

query = input("Enter Question: ")
response = input("Enter AI Response: ")

result = verify_response(query, response)

print("\n--- RESULT ---")
print("Trusted Data:", result["trusted"])
print("Final Score:", result["final_score"])
print("Decision:", result["decision"])