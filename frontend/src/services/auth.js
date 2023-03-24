import axios from "axios";

const API_URL = "http://127.0.0.1:8000/"


class AuthService {
    login(email, password) {
        return axios.post(`${API_URL}/api/token/`, {
            email,
            password
        })
        .then((response) => {
            if (response.data.access) {
                localStorage.setItem('user', JSON.stringify(response.data));
            }
            return response.data;
        })
    }

    logout() {
        localStorage.removeItem('user')
    }

    register(username, email, password) {
        return axios.post(`${API_URL}/api/register`, {
            email,
            password,
        });
    }

    getCurrentUser() {
        return JSON.parse(localStorage.getItem('user'));
    }
}

export default new AuthService();