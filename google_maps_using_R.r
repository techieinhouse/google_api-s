getGeoCode=function (gcStr)  {
  library("RJSONIO") #Load Library
  gcStr <- gsub(" ","%20",gcStr) #Encode URL Parameters
  #Open Connection
  connectStr <- paste("https://maps.googleapis.com/maps/api/geocode/json?key= &sensor=false&address=",gcStr, sep="") 
  con <- tryCatch(url(connectStr), error = function(e) NULL,warning=  function(e) NULL)
  
  data.json <- tryCatch( fromJSON(paste(readLines(con), collapse="")), error = function(e) NULL,warning=  function(e) NULL)
  close(con)
  #Flatten the received JSON
  data.json <- unlist(data.json)
  if(is.null(data.json)==FALSE)   {
    if(data.json["status"]=="OK"){
    lat <- data.json["results.geometry.location.lat"]
    lng <- data.json["results.geometry.location.lng"]
    gcodes <- c(lat, lng)
    names(gcodes) <- c("Lat", "Lng")
    return(gcodes)
  }}
}  

geoCodes <- getGeoCode("25980 Sylt, Deutschland")