from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from jobs.models import Job, Resume
from jobs.models import Cities, JobTypes
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

# Create your views here.


def joblist(request):
    joblist = Job.objects.order_by('job_type')
    # template = loader.get_template('joblist.html')
    context = {'job_list': joblist}

    for job in joblist:
        job.city_name = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    #return HttpResponse(template.render(context))
    return render(request, 'joblist.html', context)

def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]

    except Job.DoesNotExist:
        raise Http404("Job does not exist")

    return render(request, 'job.html', {'job': job})

class ResumeDetailView(DetailView):
    """ 简历详情页 """
    model = Resume
    template_name = 'resume_detail.html'
 #   success_url = '/joblist/'


# 类视图
class ResumeCreateView(LoginRequiredMixin, CreateView):
    "简历职位页面"

    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ["username", "city", "phone",
              "email", "apply_position", "gender",
              "bachelor_school", "master_school", "major", "degree",
              "candidate_introduction", "work_experience", "project_experience"]

    # 从URL请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    # 简历跟当前用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())