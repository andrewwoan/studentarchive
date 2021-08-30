from django.shortcuts import render, redirect
from .models import Profile, UserPublications, UserPresentations
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import updateForm, UserPublicationsForm, UserPresentationsForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm


def profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(
        Q(area_of_interest__icontains=search_query) & Q(account_type='grad') | Q(name__icontains=search_query) & Q(account_type='grad'))
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles.html', context)


def profiles_undergrad(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(
        Q(area_of_interest__icontains=search_query) & Q(account_type='undergrad') | Q(name__icontains=search_query) & Q(account_type='undergrad'))
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles_undergrad.html', context)


def profiles_alum(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(
        Q(area_of_interest__icontains=search_query) & Q(account_type='alum') | Q(name__icontains=search_query) & Q(account_type='alum'))
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles_alum.html', context)


def profiles_res(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(
        Q(area_of_interest__icontains=search_query) & Q(account_type='res') | Q(name__icontains=search_query) & Q(account_type='res'))
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles_res.html', context)


def profiles_postdocs(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(
        Q(area_of_interest__icontains=search_query) & Q(account_type='post') | Q(name__icontains=search_query) & Q(account_type='post'))
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles_post.html', context)


def publications(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    publications = UserPublications.objects.filter(
        Q(title__icontains=search_query) & Q(display='display') | Q(status_date__icontains=search_query) & Q(display='display') | Q(contributors__icontains=search_query) & Q(display='display') | Q(journal_title__icontains=search_query) & Q(display='display'))

    if request.method == 'POST':
        publications = publications.order_by('contributors')
    else:
        publications = publications.order_by('-status_date')

    context = {'publications': publications}
    return render(request, 'users/publications.html', context)


def profiles_invisible(request):
    profiles = Profile.objects.filter(account_type='invisible')
    context = {'profiles': profiles}
    return render(request, 'users/profiles_undergrad.html', context)


def userProfile(request, username):
    profile = Profile.objects.get(username=username)
    publications = profile.userpublications_set.all()
    presentations = profile.userpresentations_set.all()
    context = {'profile': profile, 'publications': publications,
               'presentations': presentations}
    return render(request, 'users/user-profile.html', context)


def userProfile2(request, username):
    profile = Profile.objects.get(username=username)
    publications = profile.userpublications_set.all()
    presentations = profile.userpresentations_set.all()
    context = {'profile': profile, 'publications': publications,
               'presentations': presentations}
    return render(request, 'users/private_profile.html', context)


def userAccount(request):
    profile = request.user.profile
    publications = profile.userpublications_set.all()
    presentations = profile.userpresentations_set.all()
    context = {'profile': profile, 'publications': publications,
               'presentations': presentations}
    return render(request, 'users/account.html', context)


@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile

    form = updateForm(instance=profile)

    if request.method == 'POST':
        form = updateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account edited successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile-form.html', context)


# @login_required(login_url="login")
# def modifySkills(request, pk):
#     profile = request.user.profile
#     skills = profile.userskills_set.get(id=pk)
#     form = UserSkillsForm(instance=skills)

#     if request.method == 'POST':
#         form = UserSkillsForm(request.POST, instance=skills)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Skills updated successfully')
#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'users/skills_form.html', context)

# @login_required(login_url="login")
# def modifySkills(request):
#     profile = request.user.profile
#     form = UserSkillsForm()

#     if request.method == 'POST':
#         form = UserSkillsForm(request.POST)
#         if form.is_valid():
#             userskills = form.save(commit=False)
#             userskills.author = profile
#             userskills.save()
#             messages.success(request, 'Skills updated successfully')
#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'users/skills_form.html', context)


@login_required(login_url="login")
def addPublication(request):
    profile = request.user.profile
    form = UserPublicationsForm()

    if request.method == 'POST':
        form = UserPublicationsForm(request.POST)
        if form.is_valid():
            userpublications = form.save(commit=False)
            userpublications.author = profile
            userpublications.save()
            messages.success(request, 'Publication added successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/publication_form.html', context)


@login_required(login_url="login")
def updatePublication(request, pk):
    profile = request.user.profile
    publication = profile.userpublications_set.get(id=pk)
    form = UserPublicationsForm(instance=publication)

    if request.method == 'POST':
        form = UserPublicationsForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication updated successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/publication_form.html', context)


@login_required(login_url="login")
def deletePublication(request, pk):
    profile = request.user.profile
    publication = profile.userpublications_set.get(id=pk)
    if request.method == 'POST':
        publication.delete()
        messages.success(request, 'Publication deleted successfully')
        return redirect('account')
    context = {'object': publication}
    return render(request, 'delete.html', context)


def signIn(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'username or password is incorrect')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'username or password is incorrect')

    return render(request, 'users/registration-form.html')


def signOut(request):
    logout(request)
    messages.error(request, 'You Have Successfully Signed Out')
    return redirect('login')


def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


@login_required(login_url="login")
def addPresentation(request):
    profile = request.user.profile
    form = UserPresentationsForm()

    if request.method == 'POST':
        form = UserPresentationsForm(request.POST)
        if form.is_valid():
            userpresentations = form.save(commit=False)
            userpresentations.author = profile
            userpresentations.save()
            messages.success(request, 'Presentation added successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/presentation_form.html', context)


@login_required(login_url="login")
def updatePresentation(request, pk):
    profile = request.user.profile
    presentation = profile.userpresentations_set.get(id=pk)
    form = UserPresentationsForm(instance=presentation)

    if request.method == 'POST':
        form = UserPresentationsForm(request.POST, instance=presentation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presentation updated successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/presentation_form.html', context)


@login_required(login_url="login")
def deletePresentation(request, pk):
    profile = request.user.profile
    presentation = profile.userpresentations_set.get(id=pk)
    if request.method == 'POST':
        presentation.delete()
        messages.success(request, 'Presentation deleted successfully')
        return redirect('account')
    context = {'object': presentation}
    return render(request, 'delete.html', context)
