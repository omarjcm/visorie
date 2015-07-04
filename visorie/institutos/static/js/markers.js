cat_1 = new google.maps.MarkerImage(
    '/static/img/number_1.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

cat_2 = new google.maps.MarkerImage(
    '/static/img/number_2.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

cat_3 = new google.maps.MarkerImage(
    '/static/img/number_3.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

cat_4 = new google.maps.MarkerImage(
    '/static/img/number_4.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

cat_ns = new google.maps.MarkerImage(
    '/static/img/symbol_inter.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

cumple = new google.maps.MarkerImage(
    '/static/img/letter_s.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

no_cumple = new google.maps.MarkerImage(
    '/static/img/letter_n.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

monitoreo_agua = new google.maps.MarkerImage(
    '/static/img/monitoreo_agua.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

monitoreo_sedimento = new google.maps.MarkerImage(
    '/static/img/monitoreo_sedimento.png',
    new google.maps.Size(27,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

shadow = new google.maps.MarkerImage(
    '/static/img/shadow.png',
    new google.maps.Size(55,48),
    new google.maps.Point(0,0),
    new google.maps.Point(14,48)
);

shape = {
    coord: [18,0,20,1,21,2,22,3,23,4,24,5,25,6,25,7,25,8,26,9,26,10,26,11,26,12,26,13,26,14,26,15,26,16,26,17,26,18,25,19,25,20,25,21,24,22,24,23,23,24,23,25,22,26,21,27,21,28,20,29,20,30,19,31,19,32,18,33,18,34,17,35,17,36,16,37,16,38,15,39,15,40,14,41,14,42,14,43,14,44,13,45,13,46,13,47,13,47,13,46,13,45,12,44,12,43,12,42,11,41,11,40,11,39,10,38,10,37,9,36,9,35,8,34,8,33,7,32,7,31,6,30,6,29,5,28,4,27,4,26,3,25,3,24,2,23,2,22,1,21,1,20,0,19,0,18,0,17,0,16,0,15,0,14,0,13,0,12,0,11,0,10,0,9,1,8,1,7,2,6,2,5,3,4,4,3,5,2,6,1,8,0,18,0],
    type: 'poly'
};

imagetypes = {
    "I": cat_1,
    "II": cat_2,
    "III": cat_3,
    "IV": cat_4,
    "NULL": cat_ns,
    "CUMPLE": cumple,
    "NO CUMPLE": no_cumple,
    "monitoreo_agua": monitoreo_agua,
    "monitoreo_sedimento": monitoreo_sedimento,
};
