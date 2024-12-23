# Prompt the user for the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Check the weather condition
if weather == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif weather == 'rainy':
    print("Take an umbrella.")
elif weather == 'cold':
    print("Wear a coat.")
else:
    print("I don't understand that weather.")

