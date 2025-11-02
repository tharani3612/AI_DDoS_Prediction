from src.real_time_detection import detect_ddos

if __name__ == "__main__":
    print("AI-Based DDoS Attack Prediction - Test Run\n")

    test_data = [1500, 1200000, 450, 2.5, 120, 5]
    print("Testing Data:", test_data)
    print("Prediction Result:", detect_ddos(test_data))
