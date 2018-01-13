import resim

model = resim.Simulator()
res = model.simulate()

# %matplotlib inline
snsplt_cells = resim.plot_cells(res, subplot=True)
snsplt_drug = resim.plot_drug(res)
snsplt_fht = resim.plot_fht(res)

app = resim.create_app()
app.run()
