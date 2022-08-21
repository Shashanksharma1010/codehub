from django.shortcuts import render, HttpResponse, redirect
from .models import Genre, Post, Content
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
	genres = Genre.objects.all()
	data = request.GET
	print(data) 
	if 'back' in data:
		if data['back'] != None:
			post = Post.objects.filter(title=data['back'])
			post.delete()
	genre = request.GET.get('genre')

	if genre == None:
		posts = Post.objects.all()
	else:
		posts = Post.objects.filter(genre__name__contains=genre)

	context = {
	    'genres':genres,
	    'posts':posts
	}
		
	return render(request, 'codeblog/index.html', context)


# This view Creates a new Code Post
def AddCode(request):
	if request.method == 'POST':
		data = request.POST
		if data['genre'] != '':
			genre = Genre.objects.get(id=data['genre'])
			print(data['genre'])
		elif data['genre-new'] != '':
			genre, created = Genre.objects.get_or_create(name=data['genre-new'])
		else:
			genre = None

		if Post.objects.filter(title=data['title']).exists():
			oldpost = Post.objects.get(title=data['title'])
			postid = oldpost.id 
			oldpost = Post.objects.get(id=postid)
			oldpost.genre = genre 
			oldpost.title = data['title']
			oldpost.description = data['description']
			oldpost.importance = data['importance']
			oldpost.save()
		else:
		    post = Post.objects.create(
			genre = genre,
			title = data['title'],
			description = data['description'],
			importance = data['importance']
			)
		    post.save()	

		return redirect('content', data['title'])

	if request.method == 'GET':
		data = request.GET 
		if 'back' in data:
			post = Post.objects.get(title=data['back'])
			form = CodeForm(instance=post)
			contents = post.content_set.all()
			contents.delete()
		else:
			form = CodeForm()
			post = None

	SelectGenre = GenreSelect()

	
	context = {'Genre': SelectGenre, 'form': form, 'post':post}
	return render(request, 'codeblog/form.html', context)

# This view takes code inputs with their respective titles.
def addCodeContent(request, post):
	if request.method == 'POST':
		data = request.POST

		if 'createBlock' in data:
		    content = Content.objects.create(
		    	    post = Post.objects.get(title=post),
		    	    heading = data['heading'],
		    	    code = data['code']
		    	)
		    return redirect('content', post)
		else:
			content = Content.objects.create(
		    	    post = Post.objects.get(title=post),
		    	    heading = data['heading'],
		    	    code = data['code']
		    	)
			return redirect('/')

	form = ContentForm()
	context = {
	    "form":form,
	    "post":post
	}
	return render(request, 'codeblog/contentForm.html', context)

def ViewPost(request, pk):
	post = Post.objects.get(pk=pk)
	post_content = post.content_set.all()
	context = {
	    'post_content':post_content
	}
	return render(request, 'codeblog/Posts.html', context)

def EditPost(request, pk):
	post = Post.objects.get(pk=pk)
	form = CodeForm(instance=post)
	genre = GenreSelect(instance=post)
	formlist = []
	formId = []
	post_content = post.content_set.all()
	for content in post_content:
		contentform = ContentForm(instance=content)
		contentform.prefix = content.id
		formId.append(content.id)
		formlist.append(contentform)

	if request.method == 'POST':
		print('\n\n\n\nhello\n\n\n\n')
		data = request.POST
		_post = Post.objects.filter(pk=pk)
		_post.update(
			genre=data['genre'],
			title=data['title'],
			description = data['description'],
			importance = data['importance']
			)
		for value in formId:
			specific_content = post.content_set.filter(pk=value)
			specific_content.update(
				heading=data[f'{value}-heading'], 
				code=data[f'{value}-code'])

		messages.success(request, "Post edited successfully!")

	context = {
		'form':form ,
		'genreform':genre,
		"formlist":formlist,
		'postId':post.id
	}

	return render(request, 'codeblog/edit.html', context)

def DeletePost(request, pk):
	post = Post.objects.get(pk=pk)
	form = CodeForm(instance=post)
	if request.method == 'POST':
		data = request.POST 
		if 'delete' in data:
			post.delete()
			messages.success(request, "Post deleted successfully!")
			return redirect('index')
		else:
			return redirect('index')
	context = {
	    'form':form,
	}
	return render(request, 'codeblog/delete.html', context)

def GenrePage(request):
	genres = Genre.objects.all()
	form = GenreSelect()
	if request.method == 'POST':
		data = request.POST
		try: 
			if 'creategenre' in data:
				Genre.objects.create(name=data['genre-new'])
				messages.success(request, "New Genre is created")
			if 'deletegenre' in data:
				if data['genre'] == '':
					messages.success(request, "No entry is selected for deletion")
					print("\n\nhello\n\n")
				else:
					genre = Genre.objects.get(id=data['genre']).delete()
					messages.success(request, "Genre is deleted successfully!")
		except:
			messages.success(request, "You have submitted same form again the operation cannot be performed")
	context = {
	    'genres':genres,
	    'form':form
	}
	return render(request, 'codeblog/genrepage.html', context)