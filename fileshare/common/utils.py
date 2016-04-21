from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Paginate(object):

    def paginate(self, model, page, per_page):
    	try:
    		if int(page) < 1:
    			page = 1
    	except Exception as e:
    		page = 1
    	try:
    		if int(per_page) <1:
    			per_page = 10
    	except Exception as e:
    		per_page = 10
        queryset = model.objects.all()
        paginator = Paginator(queryset, per_page)
        try:
            pagination = paginator.page(page)
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
        try:
        	cur_page = pagination.number
        except Exception as e:
        	cur_page = 1
        response = {
            'result': pagination,
            'next': next_page,
            'previous': prev_page,
            'total_page': pagination.paginator.num_pages,
            'cur_page': cur_page,
            'per_page': per_page
        }
        return response
