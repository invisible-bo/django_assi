from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# 목록 보기
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

# 상세 보기
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

# 게시글 작성
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_form.html'  # 템플릿 경로
    fields = ['title', 'content']  # 사용자 입력 필드
    success_url = reverse_lazy('post:post_list')  # 저장 후 리디렉션 경로

    def form_valid(self, form):
        form.instance.author = self.request.user  # 현재 로그인한 사용자를 author에 설정
        return super().form_valid(form)

# 게시글 수정
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post:post_list')

# 게시글 삭제
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post:post_list')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user and not request.user.is_superuser:
            return HttpResponseForbidden("삭제 권한이 없습니다.")
        return super().dispatch(request, *args, **kwargs)
