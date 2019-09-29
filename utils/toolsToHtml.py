import pandas
import numpy as np

AREA_COLLUMN = "Area"
EXCLUDE = ["Network Hardware"]

df = pandas.read_csv('TGDTools.csv')
areas = df[AREA_COLLUMN].values
areas = np.unique(areas)

htmlStruture = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>The Gizmo Dojo</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="https://use.fontawesome.com/releases/v5.0.8/js/all.js"></script>
    <link href="style.css" rel="stylesheet">
</head>

<body>

<!-- Navigation -->
<nav class="navbar navbar-expand-md navbar-light bg-light sticky-top">
    <div class="container-fluid">
        <a class="navbar-brand" href="#"><img src="img/LogoWebsite_Retina.png"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="../#welcome">Welcome</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="../#space">About the space</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="../#team">Our team</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="../#join">Join us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="../#connect">Connect</a>
                </li>
            </ul>
        </div>
    </div>
</nav>


<div id="tools" class="container-fluid padding">
<div class="row tools text-center">
    <div class="col-12">
        [CONTENT]
    </div>
</div>

</body>
'''

htmlAccordian = '''
<div class="accordion" id="accordionExample">
    [CONTENT]
</div>
'''

htmlCard = '''
<div class="card">
    <div class="card-header" id="headingOne">
      <h5 class="mb-0">
        <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapseID" aria-expanded="true" aria-controls="collapseID">
          [TITLE]
        </button>
      </h5>
    </div>

    <div id="collapseID" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
      <div class="card-body">
        [CONTENT]
      </div>
    </div>
  </div>
'''

cards = ""
for i, area in enumerate(areas):
    if area in EXCLUDE:
        continue
    withTitle = htmlCard.replace("[TITLE]", area)
    withId = withTitle.replace("collapseID", "collapse" + str(i))

    tools = df.loc[df[AREA_COLLUMN] == area, 'Tool']
    htmlTools = "<ul>"
    for t in tools:
        htmlTools = htmlTools + '''
        <li>''' + str(t) + "</li>"
    htmlTools = htmlTools + '''
    </ul>
    '''

    new = withId.replace("[CONTENT]", htmlTools)
    cards = cards + new

accordion = htmlAccordian.replace("[CONTENT]", cards)

html = htmlStruture.replace("[CONTENT]", accordion)

print(html)
with open("../tools.html", 'w') as out:
    out.write(html)
