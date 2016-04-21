from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(queryset, page_no, per_page):
	paginator = Paginator(queryset, per_page)
	try:
		pagination = paginator.page(page_no)
	except PageNotAnInteger:
		pagination = paginator.page(1)
	except EmptyPage:
		pagination = paginator.page(paginator.num_pages)
	try:
		prev_page = pagination.previous_page_number()
	except Exception as e:
		prev_page = None
	try:
		next_page = pagination.next_page_number()
	except Exception as e:
		next_page = None
	response = {
		"objects": pagination,
		"prev_page": prev_page,
		"next_page": next_page,
		"total_page": pagination.paginator.num_pages
	}
	return response