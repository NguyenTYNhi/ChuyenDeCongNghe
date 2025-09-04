from django.http import HttpResponse

def special_case_2003(request):
    return HttpResponse("Năm 2003 có sự kiện đặc biệt!")

def year_archive(request, year):
    return HttpResponse(f"Lưu trữ năm: {year}")

def month_archive(request, year, month):
    return HttpResponse(f"Lưu trữ tháng {month}/{year}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Bài viết: {slug}, tháng {month}/{year}")

def year_archive(request, year):
    return HttpResponse(f"archive cho năm {year}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"bài viết: {slug}, tháng {month}, năm {year}")