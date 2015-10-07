tree_MC   = ROOT.TChain("IIHEAnalysis")
for file in os.listdir("path"):
    if file.endswith(".root"):
        tree_MC.Add(str("path"+file))
