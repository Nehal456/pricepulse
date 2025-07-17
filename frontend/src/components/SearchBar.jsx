const handleSearch = async () => {
    setLoading(true);
    setError('');
    
    const queryParams = new URLSearchParams({
      query: searchTerm,
      brand: selectedBrand,
      min_price: minPrice,
      max_price: maxPrice,
      sort: sortOption,
      source: sourceSite,
    });
  
    try {
      const response = await fetch(`http://127.0.0.1:5000/search?${queryParams.toString()}`);
      if (!response.ok) throw new Error('Failed to fetch products');
      
      const data = await response.json();
      onResults(data);
    } catch (err) {
      console.error(err);
      setError('Something went wrong. Please try again later.');
    } finally {
      setLoading(false);
    }
  };
  