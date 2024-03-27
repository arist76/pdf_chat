const API_HOST = process.env.API_HOST
const API_PORT = process.env.API_PORT
const BASE_API = `http://${API_HOST}:${API_PORT}/`;
export const CONSTANTS = {
	URL: {
		LOGIN: BASE_API + 'auth/token/login/',
		REGISTER: BASE_API + 'auth/users/',
		CHAT: BASE_API + 'chat/',
		FORUM: BASE_API + 'forum/',
	}
};
