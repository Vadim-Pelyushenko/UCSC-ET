# UCSC-ET

The goal is to create a service which is able to track enrollment information for
classes at UCSC(University of California Santa Cruz).

A user would be able to create an account, select some classes they want to track,
and they'll be able to see graphs which show the enrollment count for classes they
are interested in over time.
A student might, for instance, be interested in a couple of classes but cannot yet
enroll in them until their enrollment appointment. If he attempts to enroll in one
he might lose his chance to enroll in the other (because other people are also
waiting just the right time to add a class). With this information the student may
be better able to judge what he should and shouldn't be enrolled in.
Also it might be interesting just to look at the data.

# What do we need to do to accomplish this?
- Need to figure out how to webscrape this information from the site
  - https://pisa.ucsc.edu/class_search/
  - It is public information. You don't need a student login to view it.
  - Unfortunately, it is a Single Page Application, and is a dynamic page. We will
  need to either investigate into the requests that are made by the site to the
  server serving it, or we need to use a framework which can make a headless browser
  thing? so that we can have that javascript simulated and be able to access the
  resulting DOM.
  - For starter's we can try to just straight up get the relevant data once. Then
  we need to make a program which can periodically scrape this data.
- Need to decide which information is relevant to scrape
  - For now, we are only interested in enrollment count for each class
- Need to implement the visualization of this information on a per class basis
- Need to create a program which will periodically request this data from the site.
  - For now, perhaps once every minute.
- Need to implement a REST API for user features and requesting the data we scrape.
