from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Category, PortfolioItem
from .forms import InquiryForm
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests


def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)

def home(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'unique_app/home.html', {'portfolio_items': portfolio_items})

def targeting_page(request):
    return render(request, 'unique_app/targeting.html')

def services(request):
    return render(request, 'unique_app/services.html')

def blog_index(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'unique_app/blog.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1  # Увеличиваем количество просмотров
    post.save(update_fields=['views'])
    # Отображение детальной информации поста
    return render(request, 'unique_app/post_detail.html', {'post': post})


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 2)  # 3 поста на каждой странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'page': page, 'posts': posts})

def post_list_by_category(request, category_slug):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.filter(available=True)
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        posts = posts.filter(categories=category)
    return render(request, 'unique_website/post/list_by_category.html', {'category': category, 'categories': categories, 'posts': posts})


def send_telegram_message(message, document=None):
    token = config('TELEGRAM_TOKEN')
    chat_id = config('TELEGRAM_CHAT_ID')

    if document:
        url = f'https://api.telegram.org/bot{token}/sendDocument'
        files = {'document': (document.name, document, document.content_type)}
        data = {'chat_id': chat_id, 'caption': message}
        response = requests.post(url, data=data, files=files)
    else:
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
        response = requests.post(url, data=params)

    return response.json()

def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            inquiry = form.save()

            message = f"""
            🔔 Новая заявка от {inquiry.full_name}!
            📞 Телефон: {inquiry.phone}
            📧 Email: {inquiry.email}
            ⚙️ Тип проекта: {inquiry.project_type}
            🔫 Описание: {inquiry.description}
            """

            send_telegram_message(message)

            if 'file' in request.FILES:
                document = request.FILES['file']
                send_telegram_message("Вам отправлен файл:", document)

            return HttpResponse('Заявка отправлена успешно!')
        else:
            return render(request, 'unique_app/inquiry_form.html', {'form': form})
    else:
        form = InquiryForm()
    return render(request, 'unique_app/inquiry_form.html', {'form': form})

def web_development(request):
    return render(request, 'unique_app/web_development.html')

def smm_services(request):
    return render(request, 'unique_app/smm_services.html')

def seo_services(request):
    return render(request, 'unique_app/seo_services.html')

def design_services(request):
    return render(request, 'unique_app/design_services.html')   

def success_view(request):
    return render(request, 'unique_app/success.html')  # Путь к вашему шаблону страницы успеха

def web_analytics(request):
    return render(request, 'unique_app/web_analytics.html')

def calculator_web(request):
    return render(request, 'unique_app/calculator-web.html')

def portfolio_detail(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, 'unique_app/portfolio_detail.html', {'item': item})

def portfolio_list(request):
    items = PortfolioItem.objects.all()
    return render(request, 'unique_app/portfolio_list.html', {'portfolio_items': items})


def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Редирект или сообщение об успехе
    else:
        form = InquiryForm()
    return render(request, 'unique_app/inquiry_form.html', {'form': form})