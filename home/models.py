from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from blog.models import BlogPage, Category, WeeklyWordPage, HowPage, Video
from cloudinary.models import CloudinaryField
from wagtailmetadata.models import MetadataPageMixin

class HomePage(MetadataPageMixin, Page):
    parent_page_types = ['wagtailcore.Page']
    template = 'home/home_page.html'
    max_count = 1
    body = RichTextField(blank=True)
    site_name = models.CharField(null=True, blank=True, max_length=100)
    site_logo = CloudinaryField("image", null=True)
    mission = RichTextField(null=True)
    vision  = RichTextField(null=True)
    caption_main_text = models.CharField(null=True, blank=True, max_length=500)
    caption_sub_text = models.CharField(null=True, blank=True, max_length=500)
    caption_image = CloudinaryField("image", null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('site_name'),
        FieldPanel('site_logo'),
        FieldPanel('mission'),
        FieldPanel('vision'),
        FieldPanel('caption_main_text'),
        FieldPanel('caption_sub_text'),
        FieldPanel('caption_image'),
    ]

    def __str__(self):
        return self.site_name
    
    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        blogs = BlogPage.objects.live().order_by('-date_created')[:11]
        recent_blogs = BlogPage.objects.live().order_by('-date_created')[:10]
        article_of_the_week = BlogPage.objects.live().filter(article_of_the_week=True).order_by('date_created').first()
        videos = Video.objects.all().order_by('-date_created')[:10   ]
        how_of_the_week = HowPage.objects.live().filter(how_of_the_week=True).order_by('-date_created').first()
        
        word_of_the_week = WeeklyWordPage.objects.live().filter(word_of_the_week=True).order_by('-date_created').first()
        categories = Category.objects.live()
        context["blogs"] = blogs
        context["recent_blogs"] = recent_blogs
        context["videos"] = videos
        context["how_of_the_week"] = how_of_the_week
        context["word_of_the_week"] = word_of_the_week
        context["article_of_the_week"] = article_of_the_week
        context["categories"] = categories
        return context
    
class AboutPage(MetadataPageMixin, Page):
    template = 'home/about.html'
    max_count = 1
    image = CloudinaryField("image", null=True)
    about_scripture_reference = models.CharField(max_length=500, null=True, blank=True)
    about_scripture_quote = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True)

    content_panels = Page.content_panels + [
        FieldPanel('about_scripture_reference'),
        FieldPanel('about_scripture_quote'),
        FieldPanel('image'),
        FieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(AboutPage, self).get_context(request, *args, **kwargs)
        recent_blogs = BlogPage.objects.live().order_by('date_created')[:4]
        about_us_article = BlogPage.objects.live().filter(about_us_article=True).order_by('date_created').first()
        context["recent_blogs"] = recent_blogs
        context["about_us_article"] = about_us_article
        return context
