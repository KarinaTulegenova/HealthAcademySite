// static/assets/js/function.js

// Пример базовых функций
console.log('Function.js loaded successfully');

// Автоматическое скрытие alert сообщений через 5 секунд
document.addEventListener('DOMContentLoaded', function () {
	const alerts = document.querySelectorAll('.alert');
	alerts.forEach(function (alert) {
		setTimeout(function () {
			const bsAlert = new bootstrap.Alert(alert);
			bsAlert.close();
		}, 5000);
	});
});