document.addEventListener('DOMContentLoaded', async () => {
  try {
    const response = await fetch('http://localhost:8000/api/options');
    if (!response.ok) throw new Error('Failed to fetch options');
    const data = await response.json();
    
    window.validLocations = new Set(data.locations);
    
    const locationInput = document.getElementById('location');
    const locationDatalist = document.getElementById('locations-list');
    locationInput.placeholder = "Search location... e.g. Whitefield";
    
    data.locations.forEach(opt => {
      const option = document.createElement('option');
      option.value = opt;
      locationDatalist.appendChild(option);
    });
    
    const populateSelect = (id, options, defaultText) => {
      const select = document.getElementById(id);
      select.innerHTML = `<option value="" disabled selected>${defaultText}</option>`;
      options.forEach(opt => {
        const option = document.createElement('option');
        option.value = opt;
        option.textContent = opt;
        select.appendChild(option);
      });
    };

    populateSelect('size', data.sizes, 'Select BHK/Size');
    populateSelect('availability', data.availabilities, 'Select availability');
    
  } catch (error) {
    console.error('Error fetching options:', error);
    // Fallbacks if backend is not running or failed
    document.getElementById('location').placeholder = 'Failed to load options. Please type manually.';
    document.getElementById('size').innerHTML = '<option value="">Failed to load.</option>';
    document.getElementById('availability').innerHTML = '<option value="">Failed to load.</option>';
  }
});

document.getElementById('prediction-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const submitBtn = document.getElementById('submit-btn');
  const resultContainer = document.getElementById('result-container');
  const priceElement = document.getElementById('predicted-price');
  
  // Set loading state
  submitBtn.classList.add('loading');
  resultContainer.classList.add('result-hidden');
  
  // Gather form data
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());
  
  // Custom validation for location
  if (window.validLocations && window.validLocations.size > 0 && !window.validLocations.has(data.location)) {
    alert("Please select a valid location from the dropdown suggestions.");
    submitBtn.classList.remove('loading');
    resultContainer.classList.add('result-hidden');
    return;
  }
  
  // Convert numerical fields
  data.bath = parseFloat(data.bath);
  data.balcony = parseFloat(data.balcony);
  if (!data.society) {
    data.society = null;
  }
  
  try {
    const response = await fetch('http://localhost:8000/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    
    if (!response.ok) {
      throw new Error('Prediction request failed');
    }
    
    const result = await response.json();
    
    // Animate number
    animateValue(priceElement, 0, result.predicted_price, 1500);
    
    // Show result
    resultContainer.classList.remove('result-hidden');
  } catch (error) {
    console.error('Error:', error);
    alert('Failed to get prediction. Please try again or check if the backend is running.');
  } finally {
    submitBtn.classList.remove('loading');
  }
});

function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    
    // easeOutQuart
    const easeProgress = 1 - Math.pow(1 - progress, 4);
    
    const current = start + easeProgress * (end - start);
    obj.innerHTML = current.toFixed(2);
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}
