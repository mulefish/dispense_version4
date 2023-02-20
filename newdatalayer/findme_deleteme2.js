const x = [
{"itemId":1,"mercantId_fk":13.07,"price":42,"instock":0,"brand":"Estraweeda","cbd":30.49,"desc":"Relaxed, Euphoric, Sleepy, Hungry, Happy","farm":"","harvest":"21/05/20","name":"Indica_5","strain":"Estraweeda","thc":20.17,"type":"preroll","Wt_Num":5,"product":"preroll"},
{"itemId":2,"mercantId_fk":7.2,"price":13,"instock":0,"brand":"Estraweeda","cbd":32.86,"desc":"Happy, Relaxed, Uplifted, Euphoric, Sleepy","farm":"","harvest":"23/11/20","name":"Hybrid_15","strain":"Estraweeda","thc":10.08,"type":"preroll","Wt_Num":15,"product":"preroll"},
{"itemId":3,"mercantId_fk":30.42,"price":61,"instock":0,"brand":"Red Flight","cbd":20.45,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"15/05/20","name":"Hybrid_5","strain":"Red Flight","thc":38.64,"type":"preroll","Wt_Num":5,"product":"preroll"},
{"itemId":4,"mercantId_fk":86.0,"price":84,"instock":0,"brand":"Estraweeda","cbd":16.07,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"02/02/19","name":"Hybrid_5","strain":"Estraweeda","thc":38.66,"type":"preroll","Wt_Num":5,"product":"preroll"},
{"itemId":5,"mercantId_fk":77.81,"price":28,"instock":0,"brand":"Estraweeda","cbd":36.29,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"23/04/20","name":"Hybrid_15","strain":"Estraweeda","thc":13.8,"type":"preroll","Wt_Num":15,"product":"preroll"},
{"itemId":6,"mercantId_fk":70.15,"price":11,"instock":0,"brand":"Silky","cbd":39.87,"desc":"Relaxed, Sleepy, Euphoric, Happy, Uplifted","farm":"","harvest":"15/04/20","name":"Indica_10","strain":"Silky","thc":19.99,"type":"preroll","Wt_Num":10,"product":"preroll"},
{"itemId":7,"mercantId_fk":68.33,"price":72,"instock":0,"brand":"Silky","cbd":28.85,"desc":"Relaxed, Euphoric, Sleepy, Hungry, Happy","farm":"","harvest":"17/01/21","name":"Indica_10","strain":"Silky","thc":23.38,"type":"preroll","Wt_Num":10,"product":"preroll"},
{"itemId":8,"mercantId_fk":43.99,"price":94,"instock":0,"brand":"Red Flight","cbd":26.13,"desc":"Euphoric, Uplifted, Relaxed, Talkative, Happy","farm":"","harvest":"27/09/21","name":"Sativa_15","strain":"Red Flight","thc":11.79,"type":"preroll","Wt_Num":15,"product":"preroll"},
{"itemId":9,"mercantId_fk":74.8,"price":58,"instock":0,"brand":"Silky","cbd":24.8,"desc":"Happy, Relaxed, Sleepy, Euphoric, Creative","farm":"","harvest":"21/09/21","name":"Indica_15","strain":"Silky","thc":26.28,"type":"preroll","Wt_Num":15,"product":"preroll"},
{"itemId":10,"mercantId_fk":85.11,"price":17,"instock":0,"brand":"Estraweeda","cbd":39.3,"desc":"Happy, Relaxed, Sleepy, Euphoric, Creative","farm":"","harvest":"12/09/21","name":"Indica_10","strain":"Estraweeda","thc":34.48,"type":"preroll","Wt_Num":10,"product":"preroll"},
{"itemId":11,"mercantId_fk":68.78,"price":34,"instock":0,"brand":"Silky","cbd":15.06,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"02/04/20","name":"Sativa_15","strain":"Silky","thc":14.07,"type":"preroll","Wt_Num":15,"product":"preroll"},
{"itemId":12,"mercantId_fk":20.11,"price":45,"instock":0,"brand":"Red Flight","cbd":24.35,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"23/07/21","name":"Sativa_20","strain":"Red Flight","thc":39.39,"type":"preroll","Wt_Num":20,"product":"preroll"},
{"itemId":13,"mercantId_fk":29.33,"price":78,"instock":0,"brand":"Estraweeda","cbd":18.73,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"19/04/21","name":"Sativa_20","strain":"Estraweeda","thc":10.78,"type":"preroll","Wt_Num":20,"product":"preroll"},
{"itemId":14,"mercantId_fk":96.16,"price":91,"instock":0,"brand":"Red Flight","cbd":19.57,"desc":"Happy, Relaxed, Sleepy, Euphoric, Creative","farm":"","harvest":"07/08/21","name":"Indica_10","strain":"Red Flight","thc":16.66,"type":"preroll","Wt_Num":10,"product":"preroll"},
{"itemId":15,"mercantId_fk":29.2,"price":8,"instock":0,"brand":"Estraweeda","cbd":21.03,"desc":"Euphoric, Uplifted, Relaxed, Talkative, Happy","farm":"","harvest":"10/01/20","name":"Sativa_5","strain":"Estraweeda","thc":19.63,"type":"preroll","Wt_Num":5,"product":"preroll"},
{"itemId":16,"mercantId_fk":93.84,"price":23,"instock":0,"brand":"Silky","cbd":20.67,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"18/11/21","name":"Hybrid_15","strain":"Silky","thc":30.65,"type":"preroll","Wt_Num":15,"product":"preroll"},
{"itemId":17,"mercantId_fk":43.39,"price":59,"instock":0,"brand":"Silky","cbd":14.35,"desc":"Happy, Relaxed, Uplifted, Euphoric, Sleepy","farm":"","harvest":"05/05/19","name":"Hybrid_15","strain":"Silky","thc":36.07,"type":"preroll","Wt_Num":15,"product":"preroll"},
{"itemId":18,"mercantId_fk":0.24,"price":93,"instock":0,"brand":"Silky","cbd":10.26,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"11/07/20","name":"Sativa_20","strain":"Silky","thc":39.46,"type":"preroll","Wt_Num":20,"product":"preroll"},
{"itemId":19,"mercantId_fk":78.66,"price":79,"instock":0,"brand":"Estraweeda","cbd":25.95,"desc":"Relaxed, Sleepy, Euphoric, Happy, Uplifted","farm":"","harvest":"12/10/20","name":"Indica_5","strain":"Estraweeda","thc":31.94,"type":"preroll","Wt_Num":5,"product":"preroll"},
{"itemId":20,"mercantId_fk":60.38,"price":86,"instock":0,"brand":"Silky","cbd":33.96,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"12/10/20","name":"Sativa_5","strain":"Silky","thc":38.04,"type":"preroll","Wt_Num":5,"product":"preroll"},
{"itemId":21,"mercantId_fk":64.3,"price":75,"instock":0,"brand":"Peanut","cbd":0.09,"desc":"indoor outdoor terpenes","farm":"Noble","harvest":"10/22/19","name":"Kellog","strain":"Peanut Butt  er Pie","thc":27.3,"type":"flower","Wt_Num":1.09,"product":"flower"},
{"itemId":22,"mercantId_fk":62.76,"price":88,"instock":0,"brand":"Sunset","cbd":0.7,"desc":"indoor outdoor terpenes","farm":"HighWinds","harvest":"11/05/19","name":"Kellog","strain":"Sunset Sherbert","thc":28.4,"type":"flower","Wt_Num":1.07,"product":"flower"},
{"itemId":23,"mercantId_fk":87.07,"price":82,"instock":0,"brand":"Headdog","cbd":0.07,"desc":"indoor outdoor terpenes","farm":"Heros of the Farm","harvest":"11/14/19","name":"Kellog","strain":"Headdog","thc":26.64,"type":"flower","Wt_Num":1.04,"product":"flower"},
{"itemId":24,"mercantId_fk":42.85,"price":67,"instock":0,"brand":"OG","cbd":0.09,"desc":"indoor outdoor terpenes","farm":"Makru Farms","harvest":"10/21/19","name":"Kellog","strain":"OG KB","thc":25.03,"type":"flower","Wt_Num":1.04,"product":"flower"},
{"itemId":25,"mercantId_fk":76.24,"price":42,"instock":0,"brand":"LostCause","cbd":0,"desc":"indoor outdoor terpenes","farm":"Trichome","harvest":"11/05/19","name":"Kellog","strain":"Lost Cause","thc":22.06,"type":"flower","Wt_Num":1.08,"product":"flower"},
{"itemId":26,"mercantId_fk":92.04,"price":44,"instock":0,"brand":"AB","cbd":0.09,"desc":"indoor outdoor terpenes","farm":"Makru Farms","harvest":"10/21/19","name":"Kellog","strain":"AB KB","thc":25.03,"type":"flower","Wt_Num":1.04,"product":"flower"},
{"itemId":27,"mercantId_fk":71.43,"price":81,"instock":0,"brand":"LostLake","cbd":0,"desc":"indoor outdoor terpenes","farm":"Trichome","harvest":"11/05/19","name":"Kellog","strain":"Lost Lake","thc":22.06,"type":"flower","Wt_Num":1.08,"product":"flower"},
]

x.forEach((item)=> { 
    item["instock"] = item["price"]
    item["price"] = item["mercantId_fk"]
    let r = Math.random() > 0.5 ? 1 : 2
    item["mercantId_fk"] = r
})

let keys = [
    'itemId',  'mercantId_fk',
    'price',   'instock',
    'brand',   'cbd',
    'desc',    'farm',
    'harvest', 'name',
    'strain',  'thc',
    'type',    'Wt_Num',
    'product'
  ]

  let out = ""
  keys.forEach((key)=>{
    out += key +"|"
  })
  console.log(out)

  x.forEach((row)=> { 
    let r = ""
    keys.forEach((key)=> { 
        r += row[key] + "|"
    })
    console.log(r)
  })