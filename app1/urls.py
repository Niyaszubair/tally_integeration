from django.urls import path
from.import views


urlpatterns = [
    path('',views.index1,name='index1'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('base',views.base,name='base'),
    path('companycreate',views.companycreate,name='companycreate'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('stock_group',views.stock_group,name='stock_group'),
    path('stock_group_secondary',views.stock_group_secondary,name='stock_group_secondary'),
    path('liststockgroupviews',views.liststockgroupviews,name='liststockgroupviews'),
    path('unit_creation',views.unit_creation,name='unit_creation'),
    path('createcategory',views.createcategory,name='createcategory'),
    path('savestockcategory',views.savestockcategory,name='savestockcategory'),
    path('catgroupsummary',views.catgroupsummary,name='catgroupsummary'),
    path('stock_items',views.stock_items,name='stock_items'),
    path('liststockviews',views.liststockviews,name='liststockviews'),
    path('godown_secondary',views.godown_secondary,name='godown_secondary'),
    path('singlestockgroupanalysisview/<int:pk>',views.singlestockgroupanalysisview,name='singlestockgroupanalysisview'),
    path('itemmovementanalysisview',views.itemmovementanalysisview,name='itemmovementanalysisview'),
    path('purchasevoucheranalysisview/<int:pk>',views.purchasevoucheranalysisview,name='purchasevoucheranalysisview'),
    path('salevoucheranalysisview/<int:pk>',views.salevoucheranalysisview,name='salevoucheranalysisview'),
    path('querystockview/<int:pk>',views.querystockview,name='querystockview'),
    path('stockgroupanalysisview',views.stockgroupanalysisview,name='stockgroupanalysisview'),

    # noufal

    path('grouppage',views.grouppage,name='grouppage'),
    path('creategroup',views.creategroup,name="creategroup"),
    path('creategroupviews',views.creategroupviews,name="creategroupviews"),
    path('groupanalisys/<int:pk>',views.groupanalisys,name="groupanalisys"),
    path('groupitem/<int:pk>',views.groupitem,name="groupitem"),
    path('createledgerviews',views.createledgerviews,name="createledgerviews"),
    path('ledgercreate',views.ledgercreate,name="ledgercreate"),
    path('selectledgerpage',views.selectledgerpage,name="selectledgerpage"),
    path('ledgerpage/<int:pk>',views.ledgerpage,name="ledgerpage"),
    path('ledgeritem/<int:pk>',views.ledgeritem,name="ledgeritem"),
    
]