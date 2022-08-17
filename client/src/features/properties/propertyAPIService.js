import axios from "axios";

//get properties
const getProperties = async () => {
	const response = await axios.get("http://127.0.0.1:8000/api/v1/properties/all/");
	return response.data;
};

const propertyAPIService = { getProperties };

export default propertyAPIService;
