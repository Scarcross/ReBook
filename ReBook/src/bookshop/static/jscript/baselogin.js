$(document)
		.ready(
				(function($) {
					// constants
					var SHOW_CLASS = 'show', HIDE_CLASS = 'hide', ACTIVE_CLASS = 'active';

					$('.tabs').ready(
							function() {
								//get the current tab
								var $curtab = $(this).find("[href='"+js_data +"']");
								//remove the current active element
								$('.active').removeClass(ACTIVE_CLASS);
								
								//switch current tab to be active
								$curtab.addClass(ACTIVE_CLASS);
								$('.show').removeClass(SHOW_CLASS).addClass(
										HIDE_CLASS);
								$(js_data).removeClass(HIDE_CLASS).addClass(
										SHOW_CLASS);
							});

					$('.tabs').on(
							'click',
							'li a',
							function(e) {
								e.preventDefault();
								var $tab = $(this), href = $tab.attr('href');
								console.log($tab);
								$('.active').removeClass(ACTIVE_CLASS);
								$tab.addClass(ACTIVE_CLASS);

								$('.show').removeClass(SHOW_CLASS).addClass(
										HIDE_CLASS).hide();

								$(href).removeClass(HIDE_CLASS).addClass(
										SHOW_CLASS).hide().fadeIn(500);
							});

				}));

