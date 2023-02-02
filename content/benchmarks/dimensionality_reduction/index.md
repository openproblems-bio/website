---
title: "Dimensionality reduction for visualisation"
summary: "Reduction of high-dimensional datasets to 2D for visualization & interpretation"
bibliography: "../../../static/bibliography/main.bib"
---

<script src="index_files/libs/htmlwidgets-1.5.4/htmlwidgets.js"></script>
<link href="index_files/libs/datatables-css-0.0.0/datatables-crosstalk.css" rel="stylesheet" />
<script src="index_files/libs/datatables-binding-0.25/datatables.js"></script>
<script src="index_files/libs/jquery-3.6.0/jquery-3.6.0.min.js"></script>
<link href="index_files/libs/dt-core-1.11.3/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="index_files/libs/dt-core-1.11.3/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="index_files/libs/dt-core-1.11.3/js/jquery.dataTables.min.js"></script>
<link href="index_files/libs/dt-ext-select-1.11.3/css/select.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-select-1.11.3/js/dataTables.select.min.js"></script>
<link href="index_files/libs/dt-ext-searchpanes-1.11.3/css/searchPanes.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-searchpanes-1.11.3/js/dataTables.searchPanes.min.js"></script>
<script src="index_files/libs/jszip-1.11.3/jszip.min.js"></script>
<link href="index_files/libs/dt-ext-buttons-1.11.3/css/buttons.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/dataTables.buttons.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.html5.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.colVis.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.print.min.js"></script>
<link href="index_files/libs/dt-ext-responsive-1.11.3/css/responsive.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-responsive-1.11.3/js/dataTables.responsive.min.js"></script>
<link href="index_files/libs/crosstalk-1.2.0/css/crosstalk.min.css" rel="stylesheet" />
<script src="index_files/libs/crosstalk-1.2.0/js/crosstalk.min.js"></script>
<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


## Description

Missing 'task_description'

## Summary

    Warning: Removed 8 rows containing missing values (geom_rect).

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="902" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true"><strong>Overview of the results per method</strong>. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Scaled scores

<div id="htmlwidget-f4d39eb6b60b395b2f81" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-f4d39eb6b60b395b2f81">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons","Responsive"],"data":[["<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP PCA (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#pearson1901pca\">Principle Component Analysis (PCA) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#vandermaaten2008visualizing\">t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (logCPM)<\/a>","<a href=\"/bibliography#mcinnes2018umap\">UMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (gamma=0)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP PCA (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#pearson1901pca\">Principle Component Analysis (PCA) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#vandermaaten2008visualizing\">t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (logCPM)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (default)<\/a>","<a href=\"/bibliography#mcinnes2018umap\">UMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (Default)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (gamma=0)<\/a>","<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (default)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (logCPM)<\/a>","<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (Default)<\/a>","<a href=\"/bibliography#vandermaaten2008visualizing\">t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP PCA (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#mcinnes2018umap\">UMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#pearson1901pca\">Principle Component Analysis (PCA) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (logCPM)<\/a>","<a href=\"/bibliography#vandermaaten2008visualizing\">t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (Default)<\/a>","<a href=\"/bibliography#pearson1901pca\">Principle Component Analysis (PCA) (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#narayan2021assessing\">densMAP PCA (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#mcinnes2018umap\">UMAP (logCPM, 1kHVG)<\/a>","<a href=\"/bibliography#xiong2020neuralee\">NeuralEE (CPU) (Default)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (gamma=0)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (default)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (gamma=0)<\/a>","<a href=\"/bibliography#moon2019visualizing\">PHATE (default)<\/a>"],["<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","Overall mean","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","Overall mean","<a href=\"/bibliography#nestorowa2016single\">Mouse hematopoietic stem cell differentiation<\/a>","Overall mean","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","Overall mean","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","Overall mean","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#olsson2016single\">Mouse myeloid lineage differentiation<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2019pbmc\">5k Peripheral blood mononuclear cells<\/a>"],[18.5855206306096,18.3624032242177,15.9427976706762,15.3557490425553,14.6241273579929,13.3162000045953,12.7724610983209,7.40563920423455,6.99961974968438,6.232239041377,6.15583401704625,5.87814265146487,5.75346854161411,5.40277364231242,4.97543622036603,4.94847806936693,3.10462688053209,2.34858539392477,2.09128708504196,1.80741453916088,1.75497054374445,1.65607931876433,1.55305024564858,1.54010989705206,1.46633766292402,1.36435892029691,1.27209710453851,1.20877858358819,1.20217384151961,1.13715037859752,1.0832280212009,1.07749760093055,1.07650507031967,1.05836671753849,0.864194526191725,0.786113474830351,0.576778510314192,0.493420966734768,0.236738630083124,-0.0466135696181709],[102.838144815093,98.6632656844972,87.2813554487485,85.7174037679864,83.8734686310011,81.2761983541781,77.0403696678397,36.5282121398929,34.9840614765618,35.1551121696587,31.0944591231848,30.3743143442016,29.9452719241385,28.9163305168673,26.0457606571869,27.433341456078,17.1172069540908,13.0506760966249,1.69154508499116,9.85425743004141,1.61500982630526,6.87408936372338,4.57592652682378,5.05494651959448,4.61903906289398,4.85599720017276,1.43292154501538,3.92445181677393,3.95016310390787,3.85778337011866,1.38642061459073,2.51631614304245,1.45537616071056,1.38298285791186,1.33520288362035,0.98874499403693,1.34719022195617,0.943250186781009,2.64972589825975,2.57376144615636],[0.700414718818407,0.847768056727686,0.821028573909878,0.56306526400129,0.295596080391196,-0.00159837231764751,-0.0337111528217687,1.46651475650676,1.75259738306546,-0.218390606322705,1.29494444268069,1.17544219479894,-0.121129600752533,1.20049585417406,-0.413832630009919,-0.448009843274678,0.232614865165247,-0.382031392037815,3.21843575077129,-0.160523219366801,3.51418558996886,0.239629332206888,0.0959591224257708,0.480693799930595,0.786064062155749,0.762907400715401,3.64711669175331,-0.00403773616050328,0.376597413041954,0.0889003448709662,-0.754944005074565,0.49548002226445,2.58666390735357,2.27774069197645,-1.30628064084176,-0.00920689080903302,-1.2017507573859,-0.383754448645021,0.274047187595165,0.316017420554536],[2.48472336911643,3.57638315441784,4.78943022295624,2.37737407101569,5.75722543352601,3.84640792733278,4.77043765483072,1.81430566993784,1.91247451612686,1.56234516928159,2.41078771481236,1.38730308549592,2.9443205825561,2.31222656818571,1.4822460776218,2.46058544475506,0.815854665565648,1.22106093640649,1.84910040626814,1.1815825995889,1.78946604759141,0.866610380782935,1.91264867630132,1.10909323442896,1.42319989768513,1.26333290702136,0.897707486941381,1.58229952679371,0.799334953318839,1.30080572963295,1.16308763784098,0.81967003453127,0.985200232153221,1.01973302379571,1.02901915264074,0.964306442251886,0.86564132327336,0.863755078351712,1.23519631666454,1.1987466427932],[16.1329439429044,15.2842773192177,11.8975099523392,14.6817450254908,9.35849443554912,8.61299260311896,7.78577845984148,6.3177593613851,5.79026249325329,5.98392446534212,4.45620238169465,5.81689525181588,3.81969324769931,3.54099362930839,5.31562486538094,3.20304674188111,3.62556948955905,2.27344206133997,1.30114519558925,2.0193505986153,0.564158635578817,1.52281222580164,1.2826551575571,1.51918894566164,1.11770922757902,1.31276602979571,0.773744130746498,1.07185735903386,1.56620839174192,1.4458296492274,0.817930149991726,0.675746803299734,1.2027323382149,0.353387965165758,0.751504406768004,0.267120384546128,0.24737653849125,-0.0315054077792532,0.589025180186546,0.773932338244202],[7.3113219795038,7.14297052350947,6.45198091819509,6.65705207245835,5.80305923242876,4.99245809904367,5.20998405385622,6.37304738061226,4.27252358444175,3.56538504871949,4.49130103190689,4.08309064185272,4.4508983313927,4.9122418946206,3.29082956597632,3.98538090482938,2.13217465530308,2.13623590386161,6.17947969078044,2.15501112794697,5.20008840735967,1.8675073046104,5.27806149852808,5.62834047155255,5.50453563803502,4.66396037566276,1.01063985415302,5.20655380532925,4.50134001518646,4.54417917745845,2.27157426322126,2.60758694470624,1.09087983791334,1.51738653949056,1.53960485530268,0.862760313821867,0.403654676029838,0.478588652142794,2.43966798683551,2.69561516572179],[2.48472336911643,3.57638315441784,4.78943022295624,2.37737407101569,5.75722543352601,3.84640792733278,4.77043765483072,1.81430566993784,1.91247451612686,1.56234516928159,2.41078771481236,1.38730308549592,2.9443205825561,2.31222656818571,1.4822460776218,2.46058544475506,0.815854665565648,1.22106093640649,1.84910040626814,1.1815825995889,1.78946604759141,0.866610380782935,1.91264867630132,1.10909323442896,1.42319989768513,1.26333290702136,0.897707486941381,1.58229952679371,0.799334953318839,1.30080572963295,1.16308763784098,0.81967003453127,0.985200232153221,1.01973302379571,1.02901915264074,0.964306442251886,0.86564132327336,0.863755078351712,1.23519631666454,1.1987466427932],[51.7158522405023,52.3461422820798,41.067048200521,39.0098650503805,32.9413105266467,28.40457957103,25.8299360386054,19.9426583684581,19.3233257794435,12.3849662107709,15.0943158264212,15.4058525551197,12.9470069341535,11.2762960400344,10.4105113762368,10.420429144935,4.95143918890035,5.2360004561512,5.77911488022727,4.32367406410099,3.30811534103642,2.77963516380444,2.0958856107652,2.33300798464477,2.00346071631249,2.09072875100546,3.53310630524509,1.91801704681135,2.2463667252456,2.11619320803691,3.80382466504867,1.52371859451785,4.96132588973297,2.21243856243023,3.51333434938829,1.86374770799513,1.75430113204739,0.844761678051287,1.56873402563533,1.71574913801483],[1.00630290563465,1.0063023346516,1.00630179458541,1.00630184557827,1.00630123058921,1.00629917611079,1.00630033577282,0.983305262571859,0.982576680986218,1.00584484896921,0.984745757345971,0.984838332310918,0.991198646028012,0.981349854013363,1.00578031129518,0.983235667730864,0.0087367301011928,0.773966073498298,1.00222579489162,0.715170184443554,1.00181487628116,0.0821091173604774,0.965600889058806,0.941387087189307,0.946901925830622,0.93983463154508,1.00159307676197,0.941988531873255,0.946106480580258,0.935935509648142,1.00169381843602,0.24068977682304,1.00210667077423,1.00103355162188,1.00141813554652,-0.00309915484280099,0.98587662539641,0.985205235738637,0.330176746129278,0.154525006296842],[0.892718110715073,0.867251298827098,0.900335894150699,0.884723230857813,0.945427305409772,0.836543092675547,0.934483470388201,-1.74145978983907,-1.49771951070814,0.844612003203242,-1.32140386112187,-2.39987019299488,-1.07831480592184,-2.03139199070372,0.66681676483137,-1.65372308668888,0.900259776970428,-2.76934348262701,-2.63872343615057,-3.91638580399448,-1.98727968663513,0.744553331579936,-3.37378253558114,-3.47837404408172,-3.89576591801744,-4.15429208606111,-1.20611774489039,-4.88220422901771,-3.83586608995513,-4.94343937815158,-0.806589187594164,0.294803503234142,-4.24846771988732,-0.968781559498879,-1.01344850143712,1.03859671453524,-0.407855352100199,-0.53549183342733,-8.74478709898409,-11.8804823433875],[0.288060854691505,0.313288433830955,0.4235554784001,0.282586026768442,0.50316527086062,0.341711667447768,0.410594800065199,0.557743222881829,0.56362057754625,0.476245934865862,0.642200038725411,0.566257216551996,0.691419574291213,0.606967488438269,0.468379137519174,0.639908818668359,0.446557814099505,0.724786349623599,0.681447076782878,0.720425810644042,0.754680352366659,0.717236586990279,0.784898834305617,0.703721737171105,0.735032119080467,0.645021086090367,0.73255221271743,0.746560187651076,0.67215246880951,0.72451044550038,0.786194617707403,0.781294152355051,0.744033154078037,0.768012518695667,0.762571468288803,0.923857794516281,0.907709372160254,0.905645447782134,0.790403741844682,0.787252846630816],[1569,320,320,439,286,729,449,1391.66666666667,333.333333333333,789,370,429,502.333333333333,759,779,455.666666666667,354,839,1559,729.666666666667,569,956,855,1047,320,360,320,459,409,979,366,955,439,470,459,1559,569,331,1159,1079],[321,112.4,128.7,30.3,1357.7,410.3,96.8,609.733333333333,159.733333333333,291.1,180.566666666667,34.1,682.366666666667,424.133333333333,269.3,95.5333333333333,1192,376.266666666667,316.4,328.266666666667,355.4,884.866666666667,332.8,1191.8,187.6,266.3,100.5,144.7,47.7,506.7,356.6,1142,24.3,225.4,45.1,320.6,256,247.1,581.7,468.4],[0.90166015625,0.8580078125,0.85751953125,0.865234375,0.8580078125,0.8580078125,0.865234375,0.741243489583333,0.6310546875,0.8580078125,0.61484375,0.5767578125,0.671028645833333,0.689290364583333,0.85791015625,0.678873697916667,2.34375,0.733756510416667,0.577734375,0.734309895833333,0.4291015625,2.34375,0.76328125,0.7443359375,0.5732421875,0.6140625,0.42109375,0.7693359375,0.4986328125,0.78076171875,0.391796875,2.63671875,0.36640625,0.41376953125,0.40205078125,2.05078125,0.48486328125,0.4861328125,0.8583984375,0.85888671875],["<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE\">v0.1<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE\">v0.1<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE\">v0.1<\/a>","<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html\">v1.0.2<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE\">v0.1<\/a>","<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html\">v1.0.2<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/lmcinnes/umap\">v0.5.3<\/a>","<a href=\"https://github.com/HiBearME/NeuralEE\">v0.1.6<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>","<a href=\"https://github.com/KrishnaswamyLab/PHATE/\">v1.0.9<\/a>"]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>continuity<\/th>\n      <th>density preservation<\/th>\n      <th>local continuity meta criterion<\/th>\n      <th>global property<\/th>\n      <th>local property<\/th>\n      <th>co-KNN size<\/th>\n      <th>co-KNN AUC<\/th>\n      <th>RMSE<\/th>\n      <th>RMSE (spectral)<\/th>\n      <th>trustworthiness<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n      <th>Library<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":14,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":13,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":15,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":9,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":10,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":11,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":12,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filters"}},"order":[],"autoWidth":false,"orderClasses":false,"responsive":true}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render","options.columnDefs.7.render","options.columnDefs.8.render","options.columnDefs.9.render","options.columnDefs.10.render","options.columnDefs.11.render","options.columnDefs.12.render","options.columnDefs.13.render"],"jsHooks":[]}</script>

## Downloads

<a href="data/task_info.json" class="btn btn-secondary">Task info</a>
<a href="data/method_info.json" class="btn btn-secondary">Method info</a>
<a href="data/metric_info.json" class="btn btn-secondary">Metric info</a>
<a href="data/dataset_info.json" class="btn btn-secondary">Dataset info</a>
<a href="data/results.json" class="btn btn-secondary">Results</a>
<a href="data/quality_control.json" class="btn btn-secondary">Quality control</a>

## Details

<details>
<summary>
Method descriptions
</summary>

-   **[densMAP (logCPM)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[narayan2021assessing\]](/bibliography#narayan2021assessing)

<!-- -->

-   **[densMAP (logCPM, 1kHVG)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[narayan2021assessing\]](/bibliography#narayan2021assessing)

<!-- -->

-   **[densMAP PCA (logCPM)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[narayan2021assessing\]](/bibliography#narayan2021assessing)

<!-- -->

-   **[densMAP PCA (logCPM, 1kHVG)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[narayan2021assessing\]](/bibliography#narayan2021assessing)

<!-- -->

-   **[NeuralEE (CPU) (Default)](https://github.com/HiBearME/NeuralEE)**: Missing 'method_description'. [\[xiong2020neuralee\]](/bibliography#xiong2020neuralee)

<!-- -->

-   **[NeuralEE (CPU) (logCPM, 1kHVG)](https://github.com/HiBearME/NeuralEE)**: Missing 'method_description'. [\[xiong2020neuralee\]](/bibliography#xiong2020neuralee)

<!-- -->

-   **[Principle Component Analysis (PCA) (logCPM)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)**: Missing 'method_description'. [\[pearson1901pca\]](/bibliography#pearson1901pca)

<!-- -->

-   **[Principle Component Analysis (PCA) (logCPM, 1kHVG)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)**: Missing 'method_description'. [\[pearson1901pca\]](/bibliography#pearson1901pca)

<!-- -->

-   **[PHATE (default)](https://github.com/KrishnaswamyLab/PHATE/)**: Missing 'method_description'. [\[moon2019visualizing\]](/bibliography#moon2019visualizing)

<!-- -->

-   **[PHATE (logCPM, 1kHVG)](https://github.com/KrishnaswamyLab/PHATE/)**: Missing 'method_description'. [\[moon2019visualizing\]](/bibliography#moon2019visualizing)

<!-- -->

-   **[PHATE (logCPM)](https://github.com/KrishnaswamyLab/PHATE/)**: Missing 'method_description'. [\[moon2019visualizing\]](/bibliography#moon2019visualizing)

<!-- -->

-   **[PHATE (gamma=0)](https://github.com/KrishnaswamyLab/PHATE/)**: Missing 'method_description'. [\[moon2019visualizing\]](/bibliography#moon2019visualizing)

<!-- -->

-   **[Random Features](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[True Features](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[True Features (logCPM)](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[True Features (logCPM, 1kHVG)](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCPM)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE)**: Missing 'method_description'. [\[vandermaaten2008visualizing\]](/bibliography#vandermaaten2008visualizing)

<!-- -->

-   **[t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCPM, 1kHVG)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE)**: Missing 'method_description'. [\[vandermaaten2008visualizing\]](/bibliography#vandermaaten2008visualizing)

<!-- -->

-   **[UMAP (logCPM)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[mcinnes2018umap\]](/bibliography#mcinnes2018umap)

<!-- -->

-   **[UMAP (logCPM, 1kHVG)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[mcinnes2018umap\]](/bibliography#mcinnes2018umap)

<!-- -->

-   **[UMAP PCA (logCPM)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[mcinnes2018umap\]](/bibliography#mcinnes2018umap)

<!-- -->

-   **[UMAP PCA (logCPM, 1kHVG)](https://github.com/lmcinnes/umap)**: Missing 'method_description'. [\[mcinnes2018umap\]](/bibliography#mcinnes2018umap)

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **continuity**: Missing 'metric_description'. [\[zhang2021pydrmetrics\]](/bibliography#zhang2021pydrmetrics)

<!-- -->

-   **density preservation**: Missing 'metric_description'. [\[narayan2021assessing\]](/bibliography#narayan2021assessing)

<!-- -->

-   **local continuity meta criterion**: Missing 'metric_description'. [\[zhang2021pydrmetrics\]](/bibliography#zhang2021pydrmetrics)

<!-- -->

-   **global property**: Missing 'metric_description'. [\[zhang2021pydrmetrics\]](/bibliography#zhang2021pydrmetrics)

<!-- -->

-   **local property**: Missing 'metric_description'. [\[zhang2021pydrmetrics\]](/bibliography#zhang2021pydrmetrics)

<!-- -->

-   **co-KNN size**: Missing 'metric_description'. [\[zhang2021pydrmetrics\]](/bibliography#zhang2021pydrmetrics)

<!-- -->

-   **co-KNN AUC**: Missing 'metric_description'. [\[zhang2021pydrmetrics\]](/bibliography#zhang2021pydrmetrics)

<!-- -->

-   **RMSE**: Missing 'metric_description'. [\[kruskal1964mds\]](/bibliography#kruskal1964mds)

<!-- -->

-   **RMSE (spectral)**: Missing 'metric_description'. [\[coifman2006diffusion\]](/bibliography#coifman2006diffusion)

<!-- -->

-   **trustworthiness**: Missing 'metric_description'. [\[venna2001neighborhood\]](/bibliography#venna2001neighborhood)

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **Mouse hematopoietic stem cell differentiation**: Missing 'dataset_description'. [\[nestorowa2016single\]](/bibliography#nestorowa2016single)

<!-- -->

-   **Mouse myeloid lineage differentiation**: Missing 'dataset_description'. [\[olsson2016single\]](/bibliography#olsson2016single)

<!-- -->

-   **5k Peripheral blood mononuclear cells**: Missing 'dataset_description'. [\[10x2019pbmc\]](/bibliography#10x2019pbmc)

</details>
<details>
<summary>
Baseline descriptions
</summary>

-   **Random Features**: Missing 'method_description'.

<!-- -->

-   **True Features**: Missing 'method_description'.

<!-- -->

-   **True Features (logCPM)**: Missing 'method_description'.

<!-- -->

-   **True Features (logCPM, 1kHVG)**: Missing 'method_description'.

</details>
<details>
<summary>
Quality control
</summary>
<table class="table lightable-paper" style='margin-left: auto; margin-right: auto; font-family: "Arial Narrow", arial, helvetica, sans-serif; margin-left: auto; margin-right: auto;'>
 <thead>
  <tr>
   <th style="text-align:left;"> Category </th>
   <th style="text-align:left;"> Name </th>
   <th style="text-align:right;"> Value </th>
   <th style="text-align:left;"> Condition </th>
   <th style="text-align:left;"> Severity </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> Best score neuralee_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> 102.8381448 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> Best score densmap_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> 98.6632657 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> Best score densmap_pca_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> 87.2813554 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> Best score pca_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> 85.7174038 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> Best score tsne_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> 83.8734686 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> Best score phate_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> 81.2761984 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> Best score umap_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> 77.0403697 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> Best score densmap_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> 52.3461423 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> Best score neuralee_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> 51.7158522 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> Best score densmap_pca_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> 41.0670482 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> Best score pca_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> 39.0098651 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> Best score phate_sqrt continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> 35.1551122 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> Best score tsne_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> 32.9413105 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> Best score phate_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> 28.4045796 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> Best score phate_default continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> 26.0457607 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> Best score umap_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> 25.8299360 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> Worst score phate_default rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> -11.8804823 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> Method 'densmap_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> Method 'densmap_pca_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> Method 'pca_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> Method 'phate_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> Method 'pymde_distances_log_cpm_hvg' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> Method 'pymde_distances_log_cpm' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> Method 'pymde_neighbors_log_cpm_hvg' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> Method 'pymde_neighbors_log_cpm' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> Method 'true_features_log_cpm_hvg' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> Method 'true_features_log_cpm' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> Method 'tsne_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> Method 'umap_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> Method 'umap_pca_logCPM_1kHVG' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> Method 'umap_pca_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> Worst score phate_sqrt rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> -8.7447871 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> Best score neuralee_default continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> 17.1172070 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> Best score neuralee_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> 16.1329439 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> Best score densmap_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> 15.2842773 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> Best score pca_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> 14.6817450 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> Best score phate_sqrt qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> 12.3849662 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> Best score densmap_pca_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> 11.8975100 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> Raw data </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> Number of results </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> 36.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> len(results) == len(method_info) * len(metric_info) * len(dataset_info) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> Dataset 'mouse_hspc_nestorowa2016' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> Dataset 'olsson_2016_mouse_blood' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> Dataset 'tenx_5k_pbmc' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> Metric 'continuity' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> Metric 'density_preservation' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> Metric 'lcmc' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> Metric 'qglobal' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> Metric 'qlocal' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> Metric 'qnn_auc' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> Metric 'qnn' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> Metric 'rmse_spectral' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> Metric 'rmse' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> Metric 'trustworthiness' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> Best score phate_default qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> 10.4105114 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> Worst score phate_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> -4.9434394 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> Worst score umap_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> -4.8822042 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> Best score tsne_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> 9.3584944 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> Best score phate_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> 8.6129926 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> Worst score pca_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> -4.2484677 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> Worst score densmap_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> -4.1542921 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> Worst score densmap_pca_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> -3.8957659 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> Best score umap_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> 7.7857785 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> Best score neuralee_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> 7.3113220 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> Best score densmap_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> 7.1429705 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> Worst score neuralee_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> -3.4783740 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> Worst score tsne_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> -3.3737825 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> Best score pca_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> 6.6570521 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> Best score densmap_pca_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> 6.4519809 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> Best score phate_sqrt qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> 5.9839245 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> Best score tsne_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> 5.8030592 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> Best score tsne_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> 5.7572254 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> Best score tsne_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> 5.7572254 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> Best score phate_default qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> 5.3156249 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> Best score umap_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> 5.2099841 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> Best score phate_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> 5.2000884 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> Best score neuralee_default qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> 4.9514392 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> Best score densmap_pca_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> 4.7894302 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> Best score densmap_pca_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> 4.7894302 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> Best score umap_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> 4.7704377 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> Best score umap_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> 4.7704377 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> Best score phate_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> 3.8464079 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> Best score phate_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> 3.8464079 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> Best score densmap_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> 3.6471167 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> Best score neuralee_default qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> 3.6255695 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> Best score densmap_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> 3.5763832 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> Best score densmap_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> 3.5763832 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> Best score phate_sqrt qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> 3.5653850 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> Best score phate_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> 3.5141856 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> Best score phate_default qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> 3.2908296 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> Best score neuralee_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> 3.2184358 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> Worst score umap_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> -1.3062806 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> Best score neuralee_default qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> 2.6075869 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> Best score pca_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> 2.5866639 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> Best score neuralee_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> 2.4847234 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> Best score neuralee_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> 2.4847234 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> Worst score phate_sqrt density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> -1.2017508 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> Best score pca_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> 2.3773741 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> Best score pca_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> 2.3773741 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> Best score densmap_pca_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> 2.2777407 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> ✗ </td>
  </tr>
</tbody>
</table>

</details>
<details>
<summary>
Visualization of raw results
</summary>

<img src="index.markdown_strict_files/figure-markdown_strict/raw_results-1.png" width="960" />

</details>
