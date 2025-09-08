from django.http import JsonResponse
from django.shortcuts import render

# Predefined responses (dictionary)
responses = {
    "hello": "Hi! আমি SatGPT 😎। তোমাকে সাহায্য করার জন্য তৈরি।",
    "Hello": "Hi! আমি SatGPT 😎। তোমাকে সাহায্য করার জন্য তৈরি।",
    "Hi": "Hi! আমি SatGPT 😎। তোমাকে সাহায্য করার জন্য তৈরি।",
    "hi": "Hi! আমি SatGPT 😎। তোমাকে সাহায্য করার জন্য তৈরি।",
    "how are you": "আমি ভালো আছি, তুমি কেমন আছো?",
    "your name": "আমার নাম SatGPT 🖥️",
    "What is your name?": "আমার নাম SatGPT 🖥️",
    "your name?": "আমার নাম SatGPT 🖥️",
    "what do you know?": "I have been trained on little programming  ",
    "bye": "বিদায়! আবার কথা হবে 👋",
}

def chat_view(request):
    return render(request, "satgpt/chat.html")

def get_response(request):
    user_message = request.GET.get("message", "").lower()

    # Dictionary থেকে উত্তর খোঁজা
    bot_reply = responses.get(user_message, "দুঃখিত, আমি এটা বুঝতে পারলাম না।")

    return JsonResponse({"reply": bot_reply})
