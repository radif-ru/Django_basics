Создал в ShopUserAuthenticationForm(AuthenticationForm) свойство redirect_url и отрендерил туда поле:
self.redirect_url = forms.HiddenInput().render(name='redirect_url', value=self.data['next'])
потом в шаблоне отоброжаю его, обращаясь через form.redirect_url,
можно сделать, чтобы это поле автоматически создавлось в форме, без дополнительного вызова?