import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';
import axios from 'axios';

const IPConverter = () => {
    const [ipv4, setIpv4] = useState('');
    const [ipv6, setIpv6] = useState('');
    const [error, setError] = useState('');

    const handleConvert = async () => {
        try {
            const response = await axios.post('/api/convert/', { ipv4 });
            setIpv6(response.data.ipv6);
            setError('');
        } catch (err) {
            setError('Adresse IPv4 invalide ou erreur serveur');
            setIpv6('');
        }
    };

    return (
        <Box sx={{ p: 4, maxWidth: 600, mx: 'auto', mt: 5 }}>
            <Typography variant="h4" gutterBottom>Convertisseur IPv4 vers IPv6</Typography>
            <TextField
                label="Entrez une adresse IPv4"
                value={ipv4}
                onChange={(e) => setIpv4(e.target.value)}
                fullWidth
                margin="normal"
            />
            <Button variant="contained" onClick={handleConvert} sx={{ mt: 2 }}>
                Convertir
            </Button>
            {ipv6 && (
                <Typography variant="h6" sx={{ mt: 3 }}>
                    IPv6 : {ipv6}
                </Typography>
            )}
            {error && (
                <Typography color="error" sx={{ mt: 3 }}>
                    {error}
                </Typography>
            )}
        </Box>
    );
};

export default IPConverter;