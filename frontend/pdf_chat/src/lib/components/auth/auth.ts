import { CONSTANTS } from '$lib/constants';
import axios from 'axios';

export const login = async (username: string, password: string) => {
	try {
		const response = await axios.post(CONSTANTS.URL.LOGIN, {
			username,
			password
		});

		const data = await response.data;
		localStorage.setItem('auth_token', data.auth_token);
		return true;
	} catch (error) {
		return false;
	}
};

export const register = async (username: string, email: string, password: string) => {
	try {
		await axios.post(CONSTANTS.URL.REGISTER, {
			username,
			email,
			password
		});
		return true;
	} catch (error) {
		return false;
	}
};

export const validatePassword = (password: string) => {
	const minLength = 8;
	const hasUpperCase = /[A-Z]/.test(password);
	const hasLowerCase = /[a-z]/.test(password);
	const hasNumbers = /\d/.test(password);
	const hasSpecialChars = /[!@#$%^&*(),.?":{}|<>]/.test(password);

	const isValidLength = password.length >= minLength;
	const isValidPassword = hasUpperCase && hasLowerCase && hasNumbers && hasSpecialChars;

	return isValidLength && isValidPassword;
};