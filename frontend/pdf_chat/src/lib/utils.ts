export const getCookieValue = (cookieName: string) => {
	const name = cookieName + '=';
	const decodedCookie = decodeURIComponent(document.cookie);
	const cookieArray = decodedCookie.split(';');

	for (let i = 0; i < cookieArray.length; i++) {
		const cookie = cookieArray[i].trim();
		if (cookie.indexOf(name) === 0) {
			return cookie.substring(name.length, cookie.length);
		}
	}
	return null; // Return null if the cookie with the given name is not found
};

export const scrollToBottom = () => {
	const windowHeight = window.innerHeight;
	window.scrollTo({
		top: document.body.scrollHeight + windowHeight,
		behavior: 'smooth'
	});
};
