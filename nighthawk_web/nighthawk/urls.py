from django.conf.urls import url, include, patterns
from django.contrib import admin

from nighthawk.views.home import Home, HomeSearch
from nighthawk.views.update_doc import UpdateDoc
from nighthawk.views.upload import Upload
from nighthawk.views.comment import Comment
from nighthawk.views.stack_framework import StackView, StackResponse
from nighthawk.views.timeline import TimeLine, TimeLineResponse

from nighthawk.views.datatypes.w32registryraw import W32Registry
from nighthawk.views.datatypes.w32services import W32Services
from nighthawk.views.datatypes.filedownloadhistory import FiledownloadHistory
from nighthawk.views.datatypes.w32tasks import W32Tasks
from nighthawk.views.datatypes.w32network_route import W32Network_Route
from nighthawk.views.datatypes.urlhistory import UrlHistory
from nighthawk.views.datatypes.w32network_arp import W32Network_Arp
from nighthawk.views.datatypes.w32ports import W32Ports
from nighthawk.views.datatypes.w32prefetch import W32Prefetch
from nighthawk.views.datatypes.w32useraccounts import W32UserAccounts
from nighthawk.views.datatypes.w32network_dns import W32Network_DNS
from nighthawk.views.datatypes.w32scripting_filepersistence import W32ScriptingFilePersistence
from nighthawk.views.datatypes.stateagentinspector import StateagentInspector
from nighthawk.views.datatypes.w32processestree import W32ProcessesTree
from nighthawk.views.datatypes.w32volumes import W32Volumes
from nighthawk.views.datatypes.w32apifiles import W32APIFiles
from nighthawk.views.datatypes.w32rawfiles import W32RAWFiles
from nighthawk.views.datatypes.w32system import W32System

data_types = patterns('',
    url(r'^filedownloadhistory_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', FiledownloadHistory.as_view(), name="filedownloadhistory"),
    url(r'^urlhistory_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', UrlHistory.as_view(), name="urlhistory"),
    url(r'^w32tasks_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Tasks.as_view(), name="w32tasks"),
    url(r'^w32services_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Services.as_view(), name="w32services"),
    url(r'^w32system_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32System.as_view(), name="w32system"),
    url(r'^w32registryraw_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Registry.as_view(), name="w32registryraw"),
    url(r'^w32apifiles_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32APIFiles.as_view(), name="w32apifiles"),
    url(r'^w32rawfiles_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32RAWFiles.as_view(), name="w32rawfiles"),
    url(r'^w32network-route_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Network_Route.as_view(), name="w32network_route"),
    url(r'^w32network-arp_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Network_Arp.as_view(), name="w32network_arp"),
    url(r'^w32ports_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Ports.as_view(), name="w32ports"),
    url(r'^w32prefetch_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Prefetch.as_view(), name="w32prefetch"),
    url(r'^w32useraccounts_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32UserAccounts.as_view(), name="w32useraccounts"),
    url(r'^w32network-dns_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Network_DNS.as_view(), name="w32network_dns"),
    url(r'^w32volumes_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32Volumes.as_view(), name="w32volumes"),
    url(r'^w32scripting-persistence_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32ScriptingFilePersistence.as_view(), name="w32network_dns"),
    url(r'^stateagentinspector_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', StateagentInspector.as_view(), name="stateagentinspector"),
    url(r'^w32processes-tree_anchor/(?P<case>[^/]+)/(?P<hostname>\w+)$', W32ProcessesTree.as_view(), name="w32ptree"),
	)

urlpatterns = [
    url(r'^', include(data_types)),
    url(r'^admin/$', admin.site.urls),
    url(r'^errorpage/$', Home().Home404, name='home_404'),
    url(r'^update_doc/$', UpdateDoc.as_view(), name="update_doc"),
	url(r'^comments/get_comment_doc/dialog$', Comment().DocDiaglog, name="comments_doc_dialog"),
    url(r'^comments/get_comment_doc/$', Comment().CommentDoc, name="comments_doc"),
    url(r'^comments/$', Comment.as_view(), name="comments"),
    url(r'^upload/$', Upload.as_view(), name="upload"),
    url(r'^home/load_cases$', Home().LoadCaseTree, name="load_cases"),
    url(r'^home/load_cases_audit$', Home().LoadCaseTreeAudit, name="load_cases_audit"),
    url(r'^home/load_stack$', StackView().LoadStackTree, name="load_stack"),
    url(r'^home/load_timeline$', TimeLine().LoadTLTree, name="load_timeline"),
    url(r'^home/main_search/$', HomeSearch.as_view(), name="home_search"),
    url(r'^stack_response/$', StackResponse.as_view(), name="stack_response"),
    url(r'^stack/$', StackView.as_view(), name="stack_framework"),
    url(r'^timeline_response/$', TimeLineResponse.as_view(), name="timeline_response"),
    url(r'^timeline/$', TimeLine.as_view(), name="timeline"),
    url(r'$', Home.as_view(), name="home"),
]
