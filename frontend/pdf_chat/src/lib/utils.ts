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
	setTimeout(() => {
		window.scrollTo({
			top: document.documentElement.scrollHeight,
			behavior: 'smooth'
		});
	}, 0);
};

export const formatDateString = (dateString: string) => {
	const dateObject = new Date(dateString);

	const month = String(dateObject.getMonth() + 1).padStart(2, '0');
	const day = String(dateObject.getDate()).padStart(2, '0');
	const year = dateObject.getFullYear();
	const hours = String(dateObject.getHours()).padStart(2, '0');
	const minutes = String(dateObject.getMinutes()).padStart(2, '0');
	// const seconds = String(dateObject.getSeconds()).padStart(2, '0');

	const formattedDate = `${hours}:${minutes} ${month}/${day}/${year}`;

	return formattedDate;
};
