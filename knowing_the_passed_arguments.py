def blender(farm_id=744):
    print("[STATUS] Taking the principal components synoptic table")
    
    args = locals().copy()
    print(args)
    print(args['farm_id'])
    
    blend_core(farm_id=args['farm_id'])
    #e cosi' hai sincronizzato l'argomento farm_id tra la funzione esterna (blender) e la funzione interna blend_core

