from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Chat

# Predefined responses (dictionary)
responses = {
    "hello": "Hi! আমি SatGPT 😎। তোমাকে সাহায্য করার জন্য তৈরি।",
    "how are you": "আমি ভালো আছি, তুমি কেমন আছো?",
    "your name": "আমার নাম SatGPT 🖥️",
    "bye": "বিদায়! আবার কথা হবে 👋",
    "what are some sat math tips?": "SAT Math Tips:\n1. Master the basics: algebra, geometry, and basic trigonometry\n2. Practice with official SAT questions\n3. Learn to eliminate wrong answers\n4. Manage your time effectively\n5. Show your work to avoid careless mistakes",
    "how to improve my reading score?": "Improving SAT Reading Score:\n1. Read actively and regularly\n2. Practice identifying main ideas\n3. Learn vocabulary in context\n4. Work on time management\n5. Take practice tests regularly",
    "what's the best way to practice for the sat?": "Best SAT Practice Methods:\n1. Use official College Board materials\n2. Take full-length timed practice tests\n3. Review your mistakes thoroughly\n4. Focus on your weak areas\n5. Create a consistent study schedule",
}

@login_required
def chat_view(request):
    # Get user's chat history
    chat_history = Chat.objects.filter(user=request.user)
    return render(request, "satgpt/chat.html", {'chat_history': chat_history})

@login_required
def get_response(request):
    user_message = request.GET.get("message", "").lower()
    
    # Save user message to database
    Chat.objects.create(
        user=request.user,
        message=user_message,
        is_user=True
    )
    
    # Dictionary থেকে উত্তর খোঁজা
    bot_reply = responses.get(user_message, "দুঃখিত, আমি এটা বুঝতে পারলাম না।")
    
    # Save bot response to database
    Chat.objects.create(
        user=request.user,
        message=bot_reply,
        is_user=False
    )
    
    return JsonResponse({"reply": bot_reply})

@login_required
@csrf_exempt
def clear_chat_history(request):
    if request.method == "POST":
        # Delete all chat messages for the current user
        Chat.objects.filter(user=request.user).delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})